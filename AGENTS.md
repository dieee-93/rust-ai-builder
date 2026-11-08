# AGENTS.md — Protocolo de Trabajo para Agentes de IA

Este repositorio sigue el estándar abierto **AGENTS.md** para interacción con modelos de lenguaje y agentes autónomos (Claude Code, Cursor, Antigravity, Jules, etc.).

## 1. Misión del Proyecto
`rust-ai-builder` es un sistema de investigación e ingeniería para capturar, estructurar, verificar y procesar conocimiento sobre mecánicas de construcción y geometría en **Rust**, habilitando el diseño y optimización asistidos por IA.

---

## 2. Mapa Rápido de la Estructura
- `AGENTS.md`: Instrucciones y directivas esenciales (este archivo).
- `docs/`: Arquitectura técnica y estándares de documentación.
  - `@docs/knowledge-architecture.md`: Definición de IDs (`SRC-`, `KNW-`, `CMP-`, `MEC-`, `EXP-`), estados y tipos de evidencia.
  - `@docs/documentation-standards.md`: Convenciones formales y versionado.
  - `@docs/active-session.md`: **Punto de anclaje de la sesión actual** (leer antes de actuar).
- `decisions/`: Architecture Decision Records (ADRs). Consultar antes de proponer cambios estructurales.
- `raw/`: **[SOLO LECTURA]** Archivos de origen crudo (capturas, transcripciones, notas sucias). Nunca modificar directamente.
- `knowledge/`: **[WIKI / OBSIDIAN GRAFO]** Fichas atómicas en Markdown con Frontmatter YAML y Wikilinks bidireccionales (`[[...]]`).
- `schemas/`: Contratos formales en **JSON Schema Draft 2020-12**.
- `data/`: Registros computables estructurados consumibles por el motor.
- `tools/`: Scripts de validación, linting y mantenimiento del grafo.
- `engine/`: Futuro motor de validación geométrica y optimización.

---

## 3. Comandos de Validación
- Validar esquemas y registros de conocimiento:
  ```bash
  python tools/validate_schemas.py
  ```
- Validar integridad del grafo y enlaces rotos:
  ```bash
  python tools/validate_graph.py
  ```

---

## 4. Reglas Inviolables para Agentes ("Hard Constraints")
1. **Inmutabilidad de IDs:** Nunca inventes formatos alternativos. Usa exclusivamente:
   - `SRC-000001` (Fuentes)
   - `KNW-000001` (Conocimiento / Conceptos)
   - `CMP-000001` (Componentes del juego)
   - `MEC-000001` (Mecánicas de construcción)
   - `BLD-000001` (Diseños de base)
   - `EXP-000001` (Experimentos y pruebas)
2. **Separación Hecho vs Interpretación:** Nunca mezcles lo observado en el juego con deducciones técnicas. Usa los campos y etiquetas de evidencia correspondientes (`OFFICIAL`, `COMMUNITY`, `EXPERIMENTAL`, `REPRODUCED`, `INFERRED`).
3. **No Redecidir lo Acordado:** Consulta `decisions/` antes de sugerir reestructuraciones de formato o tooling.
4. **Respeto a Terceros:** Nunca transcribas contenidos completos de fuentes externas; referencia mediante `SRC-XXXXXX` y resume con palabras técnicas propias.
5. **Obsidian & Git First:** Todas las notas en `knowledge/` deben usar Markdown estándar, YAML frontmatter y enlaces `[[ID-slug|Alias]]`.

---

## 5. Protocolo de Inicio y Cierre de Sesión (Session Hygiene)
- **Al iniciar:**
  1. Lee `docs/active-session.md` para conocer el foco del sprint actual y tareas abiertas.
  2. Revisa `git status` para confirmar un entorno de trabajo limpio.
- **Al cerrar / entregar:**
  1. Ejecuta `python tools/validate_schemas.py` para asegurar que ningún esquema o ficha quede roto.
  2. Actualiza `docs/active-session.md` con las tareas completadas y el siguiente paso inmediato.
