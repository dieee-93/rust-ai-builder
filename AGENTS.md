# AGENTS.md — Protocolo Operativo para Agentes de IA

Este repositorio implementa el estándar abierto **AGENTS.md** para orquestación e interacción con modelos de lenguaje y agentes autónomos (Claude Code, Cursor, Antigravity, Copilot Workspace, Jules, etc.).

---

## 1. Misión y Alcance del Proyecto
`rust-ai-builder` es un sistema de investigación, modelado formal e ingeniería de conocimiento para capturar, estructurar, verificar y procesar las mecánicas de construcción y geometría del videojuego **Rust**, con el fin de habilitar el diseño asistido por IA y la optimización de bases.

---

## 2. Mapa de Arquitectura y Permisos por Directorio
| Directorio | Naturaleza | Permiso Agente | Descripción / Rol |
| :--- | :--- | :--- | :--- |
| `AGENTS.md` | Directiva raíz | Lectura | Punto de entrada y reglas operativas primarias (este archivo). |
| `docs/` | Estándares | Lectura / Edición | Especificación formal, arquitectura y seguimiento (`active-session.md`). |
| `decisions/` | ADRs | Lectura / Creación | Architecture Decision Records. Inmutables una vez aceptados. |
| `raw/` | Inmutable | **SOLO LECTURA** | Capturas, transcripciones y notas crudas. Jamás editar o borrar. |
| `knowledge/` | Vault Obsidian | Lectura / Escritura | Grafo de fichas Markdown atómicas con YAML frontmatter y wikilinks. |
| `schemas/` | Contratos | Lectura / Edición | Contratos formales en **JSON Schema Draft 2020-12**. |
| `data/` | Computable | Lectura / Escritura | Registros JSON validados consumibles por el motor. |
| `templates/` | Plantillas | Lectura / Edición | Plantillas estándar para nuevas fichas Markdown. |
| `tools/` | Herramientas | Lectura / Ejecución | Scripts de validación, linting e integridad de datos. |
| `engine/` | Motor | Lectura / Escritura | Futuro motor de validación geométrica y simulación en Rust. |

---

## 3. Entorno de Ejecución y Comandos de Validación
**Requisitos mínimos:** Python 3.10+ con dependencias `jsonschema` y `pyyaml`.

- **Validar contratos JSON Schema y registros computables:**
  ```bash
  python tools/validate_schemas.py
  ```
- **Validar integridad del Vault de Obsidian (wikilinks, frontmatter e IDs):**
  ```bash
  python tools/validate_graph.py
  ```

Ambos comandos deben finalizar con código de salida `0` (cero errores) antes de dar por terminada cualquier tarea.

---

## 4. Reglas Inviolables para Agentes ("Hard Constraints")

1. **Inmutabilidad y Formato Estricto de IDs:**
   Usa exclusivamente los prefijos canónicos con 6 dígitos secuenciales:
   - `SRC-000001` (Fuentes externas)
   - `KNW-000001` (Conceptos y principios de física/geometría)
   - `CMP-000001` (Componentes y piezas constructivas)
   - `MEC-000001` (Mecánicas y técnicas de construcción)
   - `BLD-000001` (Diseños integrales de bases)
   - `EXP-000001` (Experimentos empíricos y pruebas de laboratorio)
   *Jamás inventes formatos alternativos ni reutilices IDs existentes.*

2. **Separación Rigurosa entre Hecho e Interpretación:**
   Nunca mezcles observaciones empíricas directas con deducciones o teorías.
   Usa rigurosamente las etiquetas de evidencia:
   - `OFFICIAL`: Documentado directamente por Facepunch.
   - `COMMUNITY`: Reportado o compartido por la comunidad (Building Bulletin, YouTube).
   - `EXPERIMENTAL`: Observado en un entorno de pruebas controlado.
   - `REPRODUCED`: Reproducido y corroborado de forma independiente.
   - `INFERRED`: Hipótesis o deducción técnica aún no contrastada.

3. **Cero Alucinación de Parámetros de Juego:**
   Si un valor dimensional, rotación, socket o tolerancia es desconocido, declara explícitamente `null`. **Nunca adivines ni inventes constantes físicas o mecánicas de Rust.**

4. **Respeto a Terceros y Política Anti-Scraping:**
   - Queda terminantemente prohibido implementar bots, scrapers o automatizaciones en servidores de Discord.
   - No copies contenido protegido íntegramente. Resume con redacción técnica propia y referencia mediante `[[SRC-XXXXXX]]`.

5. **Compatibilidad Total con Obsidian (Aliases y Wikilinks):**
   - Toda nota en `knowledge/` debe residir en su subcarpeta correspondiente (`sources/`, `components/`, `mechanics/`, `concepts/`, `builds/`, `experiments/`).
   - Nombrar los archivos en kebab-case: `<ID>-<slug>.md` (ej. `CMP-000001-square-foundation.md`).
   - Todo frontmatter DEBE declarar `aliases` conteniendo el ID puro y el nombre legible para evitar enlaces rotos (*ghost notes*):
     ```yaml
     aliases:
       - CMP-000001
       - "Cimiento Cuadrado"
     ```
   - Usa wikilinks bidireccionales `[[ID-slug|Alias]]` o `[[ID|Alias]]` en el cuerpo.

6. **Precedencia de ADRs:**
   No alteres la estructura, el formato ni las herramientas sin consultar previamente `decisions/` o formalizar un nuevo Architecture Decision Record si el cambio lo amerita.

---

## 5. Protocolo de Ciclo de Vida de Sesión (Session Hygiene)

### Al Iniciar (Pre-flight Checklist)
1. Lee `docs/active-session.md` para conocer el estado actual, prioridades y siguiente paso.
2. Ejecuta `git status` para verificar un espacio de trabajo limpio.
3. Si retomas una tarea a medio hacer, ejecuta `python tools/validate_schemas.py` y `python tools/validate_graph.py` para conocer la línea base.

### Durante el Desarrollo
- Aplica **divulgación progresiva**: lee únicamente los archivos necesarios para la tarea puntual (no cargues todo el repositorio en contexto).
- Usa las plantillas de `templates/` al crear nuevas notas en `knowledge/`.
- Mantén la paridad: una ficha de conocimiento relevante debe tener su contraparte estructurada en `data/` si va a ser consumida por el motor.

### Al Cierre / Entrega (Hand-off Checklist)
1. Ejecuta `python tools/validate_schemas.py`.
2. Ejecuta `python tools/validate_graph.py`.
3. Actualiza `docs/active-session.md` marcando tareas completadas y definiendo el **siguiente paso inmediato**.
4. Ejecuta `git status` para asegurar que no queden archivos temporales sin registrar.

---

## 6. Protocolo de Gestión de Incertidumbres y Versiones
- **Cambios por parches de Rust:** Si una actualización de Facepunch invalida una mecánica, no borres el registro histórico: márcalo como `OUTDATED`, registra la versión del parche y añade notas de invalidación.
- **Fuentes en conflicto:** Si dos fuentes difieren (ej. dos creadores de contenido afirman tolerancias distintas para un pixel gap), documenta la discrepancia en la ficha; no inventes una resolución artificial sin un experimento `EXP-` que lo dirima.
