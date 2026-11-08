---
id: KNW-000001
aliases:
  - KNW-000001
  - "Estabilidad basal de cimientos"
  - "Foundation Stability"
title: "Estabilidad basal de cimientos"
category: "stability"
tags:
  - rust/stability
  - rust/foundations
status: VERIFIED
source_ids:
  - "[[SRC-000001]]"
evidence_type:
  - OFFICIAL
  - EXPERIMENTAL
game_version: "2026.0"
last_verified_at: "2026-11-08T00:00:00Z"
created_at: "2026-11-08T00:00:00Z"
updated_at: "2026-11-08T00:00:00Z"
related_knowledge:
  - "[[CMP-000001]]"
---

# Resumen

Los cimientos conectados al suelo proporcionan estabilidad estructural inicial del 100% para las entidades que se apoyan sobre ellos.

## Qué sabemos
- Un cimiento conectado al terreno inicia con 100% de estabilidad.
- La estabilidad decae de forma progresiva a medida que la estructura asciende o se aleja del anclaje al suelo.

## Afirmaciones
- **Observación:** El martillo de construcción muestra 100% en cimientos que tocan el suelo.
- **Interpretación:** La pérdida de estabilidad depende del número de pasos estructurales hacia el suelo más cercano.

## Requisitos y restricciones
- El cimiento debe estar situado a una altura válida respecto al terreno para conservar contacto de suelo.

## Entidades y Mecánicas Relacionadas
- [[CMP-000001|Square Foundation]]: Componente primario de anclaje.
- [[MEC-000001|Honeycombing triangular perimetral]]: Mecánica de refuerzo perimetral.

## Fuentes
- [[SRC-000001|Building Bulletin Welcome & Guidelines]]

## Historial de cambios
- 2026-11-08: Ficha inicial verificada con martillo en servidor Vanilla.
