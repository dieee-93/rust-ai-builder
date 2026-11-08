# Sesión Activa — rust-ai-builder

- **Última actualización:** 2026-11-08
- **Objetivo del sprint:** Establecer la infraestructura de documentación, validación de esquemas, soporte para Obsidian y primer piloto de adquisición de conocimiento.

---

## 🎯 Tareas de la Sesión Actual

- [x] Investigar y definir estrategia de documentación, modelo de grafo y relación con agentes.
- [x] Crear `AGENTS.md` (estándar abierto de instrucciones de proyecto y reglas inviolables).
- [x] Formalizar `decisions/ADR-001-knowledge-base-strategy.md` (Obsidian + Markdown Frontmatter + Wikilinks + Git).
- [x] Crear `docs/active-session.md` (anclaje de sesión).
- [x] Crear herramienta de validación de JSON Schemas y fixtures (`tools/validate_schemas.py`).
- [x] Crear e implementar herramienta de validación de integridad de grafo Obsidian (`tools/validate_graph.py`).
- [x] Validar los 6 esquemas JSON con Draft 2020-12 (`CMP`, `KNW`, `MEC`, `SRC`, `BLD`, `EXP`).
- [x] Crear contratos y plantillas completas para los 6 prefijos (`SRC-`, `KNW-`, `CMP-`, `MEC-`, `BLD-`, `EXP-`).
- [x] Refinar plantillas en `templates/` con soporte de `aliases` en frontmatter para navegación y autocompletado nativo en Obsidian.
- [x] Configurar `.gitignore` robusto (protegiendo caches de Obsidian, Python, Rust y OS).
- [x] Estructurar `knowledge/` con subcarpetas categorizadas (`sources/`, `components/`, `mechanics/`, `concepts/`, `builds/`, `experiments/`).
- [x] Crear las primeras 4 notas canónicas en `knowledge/` y verificar integridad total de grafo (16 enlaces verificados, 0 rotos).
- [ ] Ejecutar el primer piloto de adquisición manual con una técnica real de Building Bulletin.

---

## 📝 Notas y Decisiones Rápidas
- Los 6 esquemas JSON (`build`, `component`, `experiment`, `knowledge`, `mechanic`, `source`) están validados con Draft 2020-12.
- `tools/validate_schemas.py` valida tanto meta-esquemas como datos computables en `data/`.
- `tools/validate_graph.py` valida frontmatter YAML, unicidad de IDs y resolución de wikilinks contra archivos y aliases.
- `AGENTS.md` ha sido blindado con las mejores prácticas de la industria: pre-flight/post-flight checklists, permisos explícitos por carpeta, gestión de incertidumbre, anti-scraping y cero alucinación de parámetros.

---

## 🔜 Siguiente Paso Inmediato
Seleccionar y ejecutar el primer piloto de adquisición manual con una técnica real de Building Bulletin (e.g. Pixel Gap Bunker, Freeplace TC o Reverse Wall Stability).
