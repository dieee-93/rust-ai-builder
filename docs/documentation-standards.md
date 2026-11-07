# Estándares de documentación

## Convenciones

- UTF-8.
- Markdown para documentación humana.
- JSON para registros computables.
- JSON Schema Draft 2020-12 para validar contratos.
- Fechas ISO 8601 en UTC (`YYYY-MM-DDTHH:mm:ssZ`).
- IDs estables con prefijos definidos.
- Nombres de archivos en kebab-case.

## Estados y evidencia

Usar únicamente los valores enumerados en los esquemas. No inferir validación a partir de popularidad, reputación o cantidad de comentarios.

## Versionado

Registrar la versión del juego cuando se conozca. Una ficha puede seguir siendo útil históricamente aunque esté marcada `OUTDATED`.

## Cambios

- Correcciones editoriales pequeñas: actualizar el documento y su `updated_at`.
- Cambios de significado o evidencia: describirlos en el historial de cambios del registro.
- Cambios incompatibles en esquemas: incrementar la versión mayor del esquema y documentar migración.
- Nunca sobrescribir silenciosamente resultados experimentales anteriores.

## Revisión

Antes de aceptar una ficha:
- comprobar que el ID es único;
- revisar que la fuente existe y es accesible;
- separar observaciones de interpretaciones;
- indicar incertidumbres;
- verificar referencias cruzadas;
- revisar que no se incluyó material de terceros sin autorización.
