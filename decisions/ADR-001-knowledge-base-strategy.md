# ADR-001: Estrategia de Documentación, Modelo de Grafo y Gestión de Sesiones

- **Fecha:** 2026-11-08
- **Estado:** Aceptado
- **Autores:** Equipo de rust-ai-builder

---

## Contexto
El proyecto requiere modelar un dominio complejo con alta interdependencia: piezas de construcción de Rust, mecánicas geométricas (pixel gaps, freeplace, wallstacking, búnkers), fuentes de la comunidad (Building Bulletin, tutoriales), experimentos de estabilidad y representaciones computables para un futuro motor de optimización.

Necesitamos decidir:
1. El formato y tecnología de almacenamiento para la base de conocimiento y el grafo de relaciones.
2. La arquitectura para interactuar fluidamente con agentes de IA (evitando saturación de contexto y alucinaciones).
3. El protocolo para mantener la continuidad entre sesiones de trabajo sin perder contexto ni introducir desorden.

---

## Opciones Consideradas
1. **Base de datos de grafos dedicada (Neo4j / Memgraph / Triplestores RDF):**
   - *Pros:* Consultas Cypher/SPARQL avanzadas, tipado estricto.
   - *Contras:* Alta fricción de mantenimiento, difícil de auditar visualmente para humanos, sobrecarga de herramientas externas, fricción para LLMs estándar en comparación con texto plano.
2. **Notion / Coda con base de datos relacional:**
   - *Pros:* Interfaz gráfica rica.
   - *Contras:* Vendor lock-in, almacenamiento propietario fuera de Git, mala integración con herramientas CLI y agentes locales.
3. **Vault de Markdown con Frontmatter YAML + Wikilinks bidireccionales (`[[...]]`) bajo Git, visualizado con Obsidian:**
   - *Pros:* Cero lock-in; formato nativo para LLMs; visualización gráfica local inmediata sin base de datos; versionado total en Git; validable con scripts ligeros; separa capas físicas limpiamente.

---

## Decisión Aceptada

Adoptar la **Opción 3** (Patrón *LLM-Wiki / Atomic Markdown Vault*):

1. **Almacenamiento y Grafo:**
   - Todas las entidades del dominio residirán en `knowledge/` como archivos Markdown atómicos (`.md`).
   - Cada archivo tendrá un **YAML Frontmatter** con metadata obligatoria (ID estable, categoría, estado, fuentes, versión del juego).
   - Las relaciones se expresarán en el cuerpo y/o frontmatter mediante **Wikilinks estándar de Obsidian**: `[[ID-slug|Nombre Legible]]`.
2. **Separación de Tres Capas:**
   - `raw/`: Entradas inmutables originales (solo lectura).
   - `knowledge/`: Base de conocimiento procesada (lectura/escritura humana y de agentes).
   - `data/`: Modelos computables serializados en JSON validados contra `schemas/`.
3. **Protocolo con Agentes (AGENTS.md + Progressive Disclosure):**
   - La raíz contendrá `AGENTS.md` como punto de entrada compacto (<150 líneas).
   - Los agentes consultarán documentación profunda (`docs/`) únicamente bajo demanda.
4. **Higiene de Sesiones:**
   - Se mantiene un archivo `docs/active-session.md` como ancla activa de trabajo (checklist, tareas en curso, dudas abiertas y siguiente paso).
   - Toda decisión arquitectónica mayor se registrará como un nuevo ADR en `decisions/`.

---

## Consecuencias
- **Positivas:**
  - Cualquier agente o humano puede clonar el repo y entender el estado del proyecto en segundos.
  - La base de conocimiento es visualizable en Obsidian simplemente abriendo la raíz del repositorio como vault.
  - El motor de Rust (`engine/`) podrá leer directamente los esquemas y datos JSON sin depender de servicios externos en ejecución.
- **Compromisos asumidos:**
  - Es necesario implementar un script de validación (`tools/validate_schemas.py` y `tools/validate_graph.py`) para asegurar que no se introduzcan wikilinks rotos ni frontmatters inválidos.
