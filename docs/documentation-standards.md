# Estándares de documentación

## Convenciones

- **Codificación:** UTF-8 estricto.
- **Formato humano / grafo:** Markdown con YAML frontmatter y Wikilinks bidireccionales (`[[...]]`), visualizable como Vault de Obsidian.
- **Formato computable:** JSON estructurado en `data/` consumible por el motor de cálculo y simulación.
- **Validación de esquemas:** JSON Schema Draft 2020-12 en `schemas/`.
- **Validación de grafo:** `tools/validate_graph.py` para enlaces cruzados, frontmatter e integridad de IDs.
- **Fechas:** ISO 8601 en UTC (`YYYY-MM-DDTHH:mm:ssZ`).
- **Nomenclatura de archivos:** `<ID>-<slug>.md` en kebab-case (e.g., `CMP-000001-square-foundation.md`).

## Organización del Vault (`knowledge/`)

Para mantener el orden a escala sin romper la naturaleza no jerárquica del grafo, las notas se agrupan por subcarpetas según su prefijo:
- `knowledge/sources/`: Fichas de fuentes externas (`SRC-`).
- `knowledge/components/`: Piezas y entidades constructivas de Rust (`CMP-`).
- `knowledge/mechanics/`: Técnicas y mecánicas constructivas (`MEC-`).
- `knowledge/concepts/`: Principios físicos, geométricos y de juego (`KNW-`).
- `knowledge/builds/`: Diseños integrales de bases (`BLD-`).
- `knowledge/experiments/`: Pruebas empíricas y verificaciones de reproducibilidad (`EXP-`).

## Obsidian y Resolución de Wikilinks

Para garantizar que los enlaces entre notas funcionen tanto en Obsidian como en editores estándar y herramientas de validación:
1. **Frontmatter con `aliases`:** Toda ficha en `knowledge/` DEBE declarar en su YAML frontmatter:
   ```yaml
   aliases:
     - CMP-000001
     - "Cimiento Cuadrado"
     - "Square Foundation"
   ```
   Esto permite que un enlace como `[[CMP-000001]]` o `[[CMP-000001-square-foundation|Cimiento Cuadrado]]` resuelva correctamente sin crear notas fantasma (*ghost notes*).
2. **Enlaces en el cuerpo:** Usar `[[ID-slug|Texto visible]]` o `[[ID|Texto visible]]`.
3. **Enlaces en frontmatter:** Declarar siempre entre comillas para evitar conflictos de sintaxis YAML:
   ```yaml
   source_ids:
     - "[[SRC-000001]]"
   ```

## Estados y Evidencia

Usar únicamente los valores enumerados en los esquemas:
- **Estados:** `INBOX`, `PROCESSING`, `PROPOSED`, `VERIFIED`, `OUTDATED`, `REJECTED`.
- **Evidencia:** `OFFICIAL`, `COMMUNITY`, `EXPERIMENTAL`, `REPRODUCED`, `INFERRED`.
- No inferir validación a partir de popularidad, visualizaciones o cantidad de comentarios.

## Versionado y Cambios

- Registrar la versión de Rust (`game_version`) cuando se conozca explícitamente; usar `null` cuando sea incierta.
- **Correcciones menores:** Actualizar el documento y su `updated_at`.
- **Cambios de significado o evidencia:** Explicarlos en la sección de historial de cambios.
- **Incompatibilidades en esquemas:** Incrementar versión del esquema y documentar migración.
- **Resultados empíricos:** Nunca sobrescribir silenciosamente mediciones previas; si un parche modifica el comportamiento, documentar la transición o marcar la nota anterior como `OUTDATED`.

## Revisión Previa a Publicación / Fusión

Antes de considerar una ficha lista:
1. Comprobar unicidad de ID y formato regex.
2. Confirmar que la fuente existe y el locator está documentado.
3. Separar hechos y mediciones de interpretaciones o hipótesis.
4. Ejecutar `python tools/validate_schemas.py` y `python tools/validate_graph.py`.
5. Verificar que no se incorporó material con copyright de terceros sin autorización expresa.
