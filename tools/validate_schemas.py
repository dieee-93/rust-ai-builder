#!/usr/bin/env python3
"""
Validación de esquemas JSON (Draft 2020-12) y registros de datos/conocimiento para rust-ai-builder.
"""

import sys
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError, SchemaError

ROOT_DIR = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT_DIR / "schemas"
DATA_DIR = ROOT_DIR / "data"

SCHEMA_MAP = {
    "SRC": "source.schema.json",
    "KNW": "knowledge.schema.json",
    "CMP": "component.schema.json",
    "MEC": "mechanic.schema.json",
    "BLD": "build.schema.json",
    "EXP": "experiment.schema.json",
}

def load_schemas():
    validators = {}
    schema_files = list(SCHEMAS_DIR.glob("*.schema.json"))
    
    if not schema_files:
        print("[ERROR] No se encontraron archivos en schemas/")
        return None

    all_valid = True
    print(f"--- 1. Validando {len(schema_files)} Meta-Esquemas (Draft 2020-12) ---")
    for s_path in sorted(schema_files):
        try:
            with open(s_path, "r", encoding="utf-8") as f:
                schema_data = json.load(f)
            Draft202012Validator.check_schema(schema_data)
            validators[s_path.name] = Draft202012Validator(schema_data)
            print(f"  [OK] {s_path.name}")
        except (SchemaError, Exception) as e:
            print(f"  [FAIL] {s_path.name}: {e}")
            all_valid = False

    if not all_valid:
        return None
    return validators

def validate_data_records(validators):
    print("\n--- 2. Validando Registros JSON en data/ ---")
    data_files = list(DATA_DIR.glob("**/*.json")) if DATA_DIR.exists() else []
    if not data_files:
        print("  (No hay archivos JSON en data/ todavía)")
        return True

    success = True
    for d_path in sorted(data_files):
        try:
            with open(d_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            record_id = data.get("id", "")
            prefix = record_id.split("-")[0] if "-" in record_id else ""
            schema_name = SCHEMA_MAP.get(prefix)

            if not schema_name or schema_name not in validators:
                print(f"  [WARN] {d_path.relative_to(ROOT_DIR)}: ID '{record_id}' no coincide con prefijo conocido {list(SCHEMA_MAP.keys())}")
                continue

            validators[schema_name].validate(data)
            print(f"  [OK] {d_path.relative_to(ROOT_DIR)} (valida con {schema_name})")
        except ValidationError as ve:
            print(f"  [FAIL] {d_path.relative_to(ROOT_DIR)}: {ve.message}")
            success = False
        except Exception as e:
            print(f"  [ERROR] {d_path.relative_to(ROOT_DIR)}: {e}")
            success = False

    return success

def main():
    validators = load_schemas()
    if not validators:
        sys.exit(1)

    data_ok = validate_data_records(validators)
    if not data_ok:
        sys.exit(1)

    print("\n[OK] Todos los esquemas y registros JSON validados exitosamente.")
    sys.exit(0)

if __name__ == "__main__":
    main()
