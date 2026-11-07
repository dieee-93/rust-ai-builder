# Arquitectura de conocimiento

## Capas de información

1. **Fuente**: referencia a la publicación, documento, vídeo o prueba original.
2. **Registro de conocimiento**: interpretación técnica revisable, con evidencia y relaciones.
3. **Representación computable**: parámetros y estructuras que el software puede consumir.
4. **Validación**: evidencia de reproducción, límites conocidos y versión del juego.

No se debe confundir la fuente original con nuestra interpretación. Las publicaciones de terceros se referencian; no se copian íntegramente sin autorización.

## Estados

- `INBOX`: recibido, aún no procesado.
- `PROCESSING`: análisis en curso.
- `PROPOSED`: ficha elaborada, pendiente de revisión.
- `VERIFIED`: comprobado con evidencia documentada.
- `OUTDATED`: puede no corresponder a la versión actual.
- `REJECTED`: descartado, conservando el motivo y la trazabilidad cuando sea útil.

El estado documental no equivale al nivel de confianza.

## Tipos de evidencia

- `OFFICIAL`: documentación oficial del juego o del desarrollador.
- `COMMUNITY`: afirmación o técnica compartida por la comunidad.
- `EXPERIMENTAL`: observación obtenida durante una prueba.
- `REPRODUCED`: resultado reproducido de forma independiente.
- `INFERRED`: deducción técnica aún no comprobada.

## Identificadores

Usar IDs estables y no derivados del nombre del archivo:

- `SRC-000001`: fuente.
- `KNW-000001`: conocimiento general.
- `CMP-000001`: componente.
- `MEC-000001`: mecánica.
- `BLD-000001`: diseño de base.
- `EXP-000001`: experimento.

No reutilizar IDs eliminados. Los archivos pueden renombrarse sin cambiar su ID.

## Reglas de calidad

- Toda afirmación técnica importante debe tener una fuente o declararse explícitamente como hipótesis/inferencia.
- Registrar `game_version` como cadena cuando se conozca; usar `null` cuando no se conozca.
- Registrar `last_verified_at` únicamente cuando haya existido una comprobación real.
- No marcar `VERIFIED` por el mero hecho de que una publicación tenga muchos comentarios o reacciones.
- Conservar contradicciones entre fuentes; no resolverlas inventando una certeza.
- Las relaciones entre registros deben utilizar IDs, nunca rutas como identificadores primarios.
