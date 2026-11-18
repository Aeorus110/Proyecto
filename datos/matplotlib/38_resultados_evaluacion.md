# Ficha de datos: resultados de evaluación precomputados

Estos tres CSV son datos **sintéticos**, creados exclusivamente para el proyecto 38 de Matplotlib. No proceden de una evaluación real y no permiten inferir el rendimiento futuro de un sistema.

| Archivo | Filas | Uso |
| --- | ---: | --- |
| `38_curvas_evaluacion.csv` | 8 | Valor de una medida en dos conjuntos a lo largo de ocho iteraciones. |
| `38_matriz_confusion.csv` | 9 | Conteos para pares de clase real y clase predicha. Las filas conceptuales son reales; las columnas, predichas. |
| `38_metricas_clase.csv` | 3 | Precisión, cobertura y número de casos reales por clase. |

Las clases `A`, `B` y `C` son etiquetas abstractas. Las métricas de la ficha se obtienen de la matriz: precisión = diagonal / total de la columna y cobertura = diagonal / total de la fila. Se conservan con más decimales para que el alumnado pueda comprobarlas mediante `numpy.allclose`.

Los datos se distribuyen con el material didáctico; no tienen atribución ni restricciones externas.
