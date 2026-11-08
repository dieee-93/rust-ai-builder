---
id: CMP-000001
aliases:
  - CMP-000001
  - "Square Foundation"
  - "Cimiento Cuadrado"
name: "Square Foundation"
component_type: "foundation"
status: VERIFIED
description: "Standard square building foundation providing baseline 100% stability."
game_version: "2026.0"
dimensions:
  unit: "meters"
  width: 3.0
  length: 3.0
  height: 0.5
source_ids:
  - "[[SRC-000001]]"
related_knowledge: []
last_verified_at: "2026-11-08T00:00:00Z"
---

# Propiedades y Sockets

## Características físicas
- **Estabilidad transmitida:** 100% basal cuando está anclado al terreno.
- **Tiers disponibles:** Twig, Wood, Stone, Metal, Armored.

## Puntos de anclaje (Sockets y conexiones)
- `socket_wall`: Permite acoplar paredes y marcos en las 4 caras ortogonales.
- `socket_foundation`: Permite la unión coplanar con otros cimientos cuadrados y triangulares.

## Mecánicas que lo utilizan
- [[MEC-000001|Honeycombing triangular perimetral]]
- [[KNW-000001|Estabilidad basal de cimientos]]
