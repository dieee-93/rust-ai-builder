# Sesión Activa — rust-ai-builder

- **Última actualización:** 2026-11-08
- **Objetivo del sprint:** Establecer la infraestructura de documentación, validación de esquemas y primer piloto de adquisición de conocimiento.

---

## 🎯 Tareas de la Sesión Actual

- [x] Investigar y definir estrategia de documentación, modelo de grafo y relación con agentes.
- [x] Crear `AGENTS.md` (estándar abierto de instrucciones de proyecto y reglas inviolables).
- [x] Formalizar `decisions/ADR-001-knowledge-base-strategy.md` (Obsidian + Markdown Frontmatter + Wikilinks + Git).
- [x] Crear `docs/active-session.md` (anclaje de sesión).
- [x] Crear herramienta de validación de JSON Schemas y fixtures (`tools/validate_schemas.py`).
- [x] Validar los 4 esquemas JSON con Draft 2020-12 (todos superados exitosamente).
- [x] Crear ejemplos mínimos válidos para los 4 esquemas en `data/fixtures/` (`SRC-`, `CMP-`, `KNW-`, `MEC-`).
- [x] Refinar plantillas en `templates/` con soporte nativo de wikilinks de Obsidian (`knowledge.md`, `component.md`, `mechanic.md`, etc.).
- [ ] Ejecutar el primer piloto de adquisición manual con una técnica real de Building Bulletin.

---

## 📝 Notas y Decisiones Rápidas
- Los 4 esquemas JSON han sido verificados contra Draft 2020-12 mediante Python (`jsonschema`).
- Los 4 fixtures de prueba pasan la validación sin errores (`python tools/validate_schemas.py`).
- Las plantillas y la estructura de carpetas están 100% listas para ser abiertas como Vault en Obsidian.

---

## 🔜 Siguiente Paso Inmediato
Seleccionar y ejecutar el primer piloto de adquisición manual con una técnica o publicación real de Building Bulletin (e.g. Pixel Gap Bunker, Freeplace TC o Reverse Wall Stability).
