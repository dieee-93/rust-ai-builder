---
id: MEC-000001
aliases:
  - MEC-000001
  - "Honeycombing triangular perimetral"
  - "Triangle Honeycombing"
name: "Honeycombing triangular perimetral"
mechanic_type: "defensive_layering"
status: VERIFIED
purpose: "Aumentar el coste de asalto mediante cimientos triangulares y paredes que forman celdas cerradas."
principle_of_operation: "El splash damage de explosivos no atraviesa paredes estancas adyacentes."
requirements:
  - "Terreno despejado alrededor del núcleo"
  - "Material para mejora de grado (piedra o metal)"
components:
  - "[[CMP-000001]]"
game_version: "2026.0"
source_ids:
  - "[[SRC-000001]]"
related_knowledge:
  - "[[CMP-000001]]"
  - "[[KNW-000001]]"
last_verified_at: "2026-11-08T00:00:00Z"
---

# Propósito y Principio de Operación

## Descripción general
El honeycombing perimetral consiste en rodear el núcleo de la base con cimientos triangulares sellados con paredes y techos, creando cámaras de aire que obligan al atacante a gastar explosivos adicionales sin ganar acceso directo al armario de herramientas (TC) o cajas principales.

## Paso a paso de ejecución
1. **Paso 1:** Colocar cimientos triangulares acoplados al perímetro exterior del cimiento cuadrado [[CMP-000001|Square Foundation]].
2. **Paso 2:** Levantar paredes en todos los bordes externos cerrando cada celda triangular.
3. **Paso 3:** Colocar techos triangulares sobre cada celda y mejorar la estructura al tier deseado (piedra/metal).

## Comportamiento esperado
Absorbe el daño de cohetes y C4 en compartimentos aislados, impidiendo que el daño por salpicadura (*splash damage*) afecte al núcleo principal.

## Limitaciones conocidas y condiciones de fallo
- **Coste de mantenimiento:** Aumenta el upkeep diario requerido por el armario de herramientas (TC).
- **Desnivel del terreno:** En pendientes pronunciadas, los cimientos pueden quedar demasiado altos o no permitir acople.

## Referencias
- Componentes: [[CMP-000001|Square Foundation]]
- Conceptos: [[KNW-000001|Estabilidad basal de cimientos]]
- Fuentes: [[SRC-000001|Building Bulletin Welcome & Guidelines]]
