# Ficha de datos: lecturas de calidad del aire

Este fichero es un conjunto **sintético**, creado para el proyecto 30 del bloque de NumPy. No procede de una red de medición real y no debe usarse para obtener indicadores de calidad del aire ni para hacer afirmaciones sobre lugares concretos.

- Archivo: `30_lecturas_calidad_aire.csv`.
- Tamaño: 18 observaciones y 5 columnas.
- Cobertura didáctica: tres estaciones (`1`, `2` y `3`) y seis horas (`0`, `4`, `8`, `12`, `16` y `20`).
- Valores ausentes intencionados: tres, escritos como `nan`, para practicar su detección e imputación.

| Columna | Tipo previsto | Unidad | Descripción |
| --- | --- | --- | --- |
| `estacion` | entero | identificador | Estación sintética de la red. |
| `hora` | entero | horas | Hora de la lectura. |
| `temperatura_c` | decimal | °C | Temperatura simulada. |
| `humedad_pct` | decimal | % | Humedad relativa simulada. |
| `pm25_ug_m3` | decimal | µg/m³ | Concentración simulada de partículas PM2.5. |

Los datos se distribuyen con el propio material didáctico. No tienen restricciones de atribución externas.
