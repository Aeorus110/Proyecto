# Ficha de datos: canciones de alta popularidad en Spotify

## Identificación y reproducibilidad

- **Archivo:** `24_spotify_alta_popularidad.csv`.
- **Tamaño:** 1.686 filas de datos y 29 columnas.
- **Huella SHA-256:** `ba70ab2da48003ee128cb17722f2b71bd1ccbadc68f82a4b1ad176b564bbbd87`.
- **Copia local incorporada al curso:** 7 de enero de 2025, según la marca temporal del archivo recibido. Esta fecha no acredita la fecha de descarga ni la actualización de los datos.
- **Fuente y URL exacta:** [Spotify Music Dataset, Solomon Ameh (Kaggle)](https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset), fichero `high_popularity_spotify_data.csv`.
- **Revisión consultada:** 8 de septiembre de 2026. Kaggle muestra el conjunto como actualizado hace aproximadamente un año, pero la página no expone en su ficha pública una revisión inmutable. La huella SHA-256 anterior identifica exactamente la copia distribuida con el curso.
- **Método de recogida declarado por la fuente:** dos scripts de Python consultan la API de Spotify para reunir canciones populares y no populares, con atributos de audio y descriptivos.
- **Licencia declarada por la fuente:** Open Database License (ODbL) para la base de datos y Database Contents License (DbCL) para sus contenidos. Debe mantenerse la atribución a Solomon Ameh y a la fuente Kaggle; antes de redistribuir una versión adaptada, revisa las obligaciones de atribución, aviso de licencia y compartir igual de la ODbL, así como las condiciones aplicables a los datos de origen de Spotify.

## Unidad de observación y cobertura

Una fila representa una aparición de una pista en una lista de reproducción, junto con atributos de audio y metadatos. No equivale necesariamente a una canción única: hay 249 repeticiones de `track_id`, por lo que hay 1.437 pistas únicas. Las fechas de álbum van de 1954 a 2024 tras interpretación, pero el archivo no documenta cuándo, desde qué mercado ni con qué consulta se recogieron las observaciones.

La puntuación `track_popularity` observada está entre 68 y 100. Es, por diseño, una muestra de popularidad alta; no representa el catálogo completo de Spotify ni sirve para inferir qué provoca la popularidad.

## Diccionario de variables

| Variable | Tipo al cargar | Descripción y unidad |
| --- | --- | --- |
| `energy` | decimal | Intensidad y actividad percibida, escala aproximada 0–1. |
| `tempo` | decimal | Tempo estimado, en pulsos por minuto (BPM). |
| `danceability` | decimal | Adecuación al baile, escala aproximada 0–1. |
| `playlist_genre` | texto | Género asociado a la lista de reproducción. |
| `loudness` | decimal | Sonoridad media, en decibelios; los valores deben revisarse si son positivos. |
| `liveness` | decimal | Indicio de presencia de público o actuación en directo, escala aproximada 0–1. |
| `valence` | decimal | Positividad musical percibida, escala aproximada 0–1. |
| `track_artist` | texto | Artista o artistas acreditados. |
| `time_signature` | entero | Compás estimado de la pista. |
| `speechiness` | decimal | Presencia de voz hablada, escala aproximada 0–1. |
| `track_popularity` | entero | Puntuación de popularidad incluida en el archivo, de 0 a 100 en origen; aquí 68–100. |
| `track_href` | texto/URL | Enlace de API a la pista. |
| `uri` | texto | URI de Spotify de la pista. |
| `track_album_name` | texto | Nombre del álbum; existe una ausencia. |
| `playlist_name` | texto | Nombre de la lista de reproducción. |
| `analysis_url` | texto/URL | Enlace de API al análisis de audio. |
| `track_id` | texto | Identificador de la pista; permite localizar duplicados. |
| `track_name` | texto | Título de la pista. |
| `track_album_release_date` | texto | Fecha de lanzamiento del álbum; combina año, año-mes y fecha completa. |
| `instrumentalness` | decimal | Indicio de que la pista no contiene voz, escala aproximada 0–1. |
| `track_album_id` | texto | Identificador del álbum. |
| `mode` | entero | Modalidad tonal codificada (habitualmente 0 menor, 1 mayor). |
| `key` | entero | Clase tonal codificada, habitualmente de 0 a 11. |
| `duration_ms` | entero | Duración en milisegundos. |
| `acousticness` | decimal | Confianza de que la pista es acústica, escala aproximada 0–1. |
| `id` | texto | Identificador adicional; coincide con `track_id` en la copia recibida. |
| `playlist_subgenre` | texto | Subgénero asociado a la lista. |
| `type` | texto | Tipo de objeto de API; en esta copia, `audio_features`. |
| `playlist_id` | texto | Identificador de la lista de reproducción. |

Las definiciones de características de audio son las atribuidas por Spotify al origen del archivo. Son medidas y estimaciones de plataforma, no propiedades físicas completas ni categorías universales.

## Decisiones didácticas de calidad

El proyecto conserva el CSV original sin cambios. La solución crea una tabla derivada que conserva la primera aparición de cada `track_id`, convierte fechas con `format="mixed"`, calcula año y duración en minutos, y marca `loudness > 0` para revisión. No elimina valores extremos plausibles ni inventa los datos ausentes.

## Límites y uso responsable

- La selección previa por popularidad restringe el rango y puede ocultar asociaciones presentes en el catálogo completo.
- Las listas de reproducción pueden reflejar decisiones editoriales, algoritmos, mercados y periodos no documentados.
- Repetir una canción en listas cambia el peso que recibe si se analiza la tabla original.
- La popularidad es una medida de plataforma y puede cambiar con el tiempo; no se debe interpretar como calidad musical.
- Ninguna correlación del proyecto permite afirmar que un atributo de audio cause popularidad.
