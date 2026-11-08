#!/usr/bin/env python3
"""
Validación de integridad del grafo, YAML Frontmatter y Wikilinks de Obsidian para rust-ai-builder.
"""

import sys
import re
from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = ROOT_DIR / "knowledge"

VALID_STATUSES = {"INBOX", "PROCESSING", "PROPOSED", "VERIFIED", "OUTDATED", "REJECTED"}
ID_REGEX = re.compile(r"^(SRC|KNW|CMP|MEC|BLD|EXP)-[0-9]{6}$")
WIKILINK_REGEX = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]")

def extract_frontmatter(content: str):
    """Extrae el frontmatter YAML y el cuerpo de una nota markdown."""
    if not content.startswith("---"):
        return None, content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    try:
        data = yaml.safe_load(parts[1])
        return (data if isinstance(data, dict) else None), parts[2]
    except Exception as e:
        return {"_yaml_error": str(e)}, parts[2]

def extract_wikilinks(text: str) -> list[str]:
    """Extrae todos los destinos de wikilinks [[destino|alias]] o [[destino]]."""
    return [match.strip() for match in WIKILINK_REGEX.findall(text)]

def main():
    print("--- 1. Escaneando Vault de Conocimiento (Obsidian Graph) ---")
    md_files = list(KNOWLEDGE_DIR.glob("**/*.md")) if KNOWLEDGE_DIR.exists() else []

    if not md_files:
        print(f"  [INFO] No hay notas Markdown en {KNOWLEDGE_DIR.relative_to(ROOT_DIR)} todava.")
        print("  Directorio preparado y listo para recibir fichas.")
        sys.exit(0)

    print(f"  Encontradas {len(md_files)} notas en knowledge/\n")

    id_to_file = {}
    known_targets = set()
    errors = []
    warnings = []
    file_records = []

    # Pase 1: Indexar IDs, nombres de archivo y aliases
    for path in md_files:
        rel_path = path.relative_to(ROOT_DIR)
        stem = path.stem  # e.g. "CMP-000001-square-foundation"
        known_targets.add(stem)

        content = path.read_text(encoding="utf-8")
        fm, body = extract_frontmatter(content)

        if fm is None:
            warnings.append(f"{rel_path}: Sin YAML frontmatter.")
            file_records.append((path, None, content))
            continue

        if "_yaml_error" in fm:
            errors.append(f"{rel_path}: Error de sintaxis YAML: {fm['_yaml_error']}")
            file_records.append((path, None, content))
            continue

        doc_id = fm.get("id")
        if not doc_id:
            errors.append(f"{rel_path}: Falta el campo obligatorio 'id' en el frontmatter.")
        elif not ID_REGEX.match(str(doc_id)):
            errors.append(f"{rel_path}: ID '{doc_id}' no cumple con el formato estándar (SRC|KNW|CMP|MEC|BLD|EXP)-000000.")
        else:
            if doc_id in id_to_file:
                errors.append(f"ID duplicado detectado: '{doc_id}' en {rel_path} y {id_to_file[doc_id]}")
            else:
                id_to_file[doc_id] = rel_path
                known_targets.add(doc_id)

        # Indexar aliases
        aliases = fm.get("aliases", [])
        if isinstance(aliases, list):
            for alias in aliases:
                if alias:
                    known_targets.add(str(alias).strip())

        # Validar status
        status = fm.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(f"{rel_path}: Status '{status}' invlido. Opciones: {sorted(VALID_STATUSES)}")

        file_records.append((path, fm, content))

    # Pase 2: Validar enlaces rotos (wikilinks)
    print("--- 2. Validando Integridad de Wikilinks y Enlaces Cruzados ---")
    total_links = 0
    broken_links = 0

    for path, fm, full_text in file_records:
        rel_path = path.relative_to(ROOT_DIR)
        links = extract_wikilinks(full_text)
        total_links += len(links)

        for target in links:
            clean_target = target.replace('"', '').replace("'", '').strip()
            if clean_target not in known_targets:
                errors.append(f"{rel_path}: Wikilink roto '[[{target}]]' — destino no encontrado ni en archivos, ni en IDs, ni en aliases.")
                broken_links += 1

    # Reporte final
    print(f"  Total notas analizadas: {len(md_files)}")
    print(f"  Total IDs registrados: {len(id_to_file)}")
    print(f"  Total wikilinks verificados: {total_links}")

    if warnings:
        print("\n--- Advertencias ---")
        for w in warnings:
            print(f"  [WARN] {w}")

    if errors:
        print("\n--- Errores Detectados ---")
        for e in errors:
            print(f"  [FAIL] {e}")
        print(f"\n[ERROR] Se encontraron {len(errors)} problemas de integridad en el grafo.")
        sys.exit(1)

    print("\n[OK] Grafo de Obsidian 100% íntegro. Todos los enlaces y metadatos son válidos.")
    sys.exit(0)

if __name__ == "__main__":
    main()
