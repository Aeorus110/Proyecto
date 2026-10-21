# Entornos virtuales del curso

El curso utiliza varios entornos virtuales porque no todas las bibliotecas ofrecen paquetes compatibles con la misma versión de Python. Los entornos son independientes: activar uno no activa los demás y no se deben mezclar sus instalaciones.

## Mapa de entornos

| Entorno | Python | Contenido principal | Kernel de Jupyter |
| --- | --- | --- | --- |
| `.venv` | 3.14.x | Unidades generales, NumPy, Pandas, Matplotlib, Seaborn y algoritmos | `Python 3.14` |
| `.venv-tensorflow` | 3.13.x | TensorFlow/Keras (unidades 61–73 de UT5) | `Python 3.13 (TensorFlow curso)` |
| `.venv-pytorch` | 3.13.x | PyTorch, OpenCV, Matplotlib, Pandas, Seaborn y visión artificial (desde la unidad 74 de UT6) | `Python 3.13 (PyTorch curso)` |
| entorno NLP de UT7 | 3.13.x | Unidades 110–115: TensorFlow/Keras, Pandas, scikit-learn y notebooks de NLP; transformers es opcional | kernel local documentado por el profesorado |

La elección de Python 3.13 para TensorFlow se debe a la disponibilidad de sus paquetes. PyTorch se mantiene en un entorno separado para evitar que sus dependencias alteren el entorno general o el de TensorFlow. Las versiones y la compatibilidad se volverán a comprobar al publicar cada bloque.

## Regla principal

Antes de abrir un cuaderno, selecciona el kernel que corresponde a su bloque. No basta con que JupyterLab esté abierto: el kernel determina qué intérprete y qué paquetes ejecutan las celdas.

- Unidades 00–60 y bibliotecas generales de UT3: activa `.venv` y selecciona `Python 3.14`.
- Unidades 61–73 de TensorFlow/Keras: activa `.venv-tensorflow` o selecciona el kernel `Python 3.13 (TensorFlow curso)`. Consulta [entorno_tensorflow.md](entorno_tensorflow.md).
- Unidad 74 y siguientes que indiquen PyTorch: activa `.venv-pytorch` o selecciona `Python 3.13 (PyTorch curso)`. Consulta la sección siguiente.

No instales paquetes desde una celda del cuaderno. Si aparece `ModuleNotFoundError`, comprueba primero el kernel seleccionado y la versión activa antes de instalar nada.

## Fase 19 de UT7 (NLP local)

La unidad 110 necesita TensorFlow/Keras y NumPy; las unidades 112–115 necesitan además Pandas y scikit-learn. Se puede usar un entorno 3.13 del curso que contenga esas dependencias, o preparar un entorno específico siguiendo el mismo procedimiento de `ipykernel` mostrado arriba. La unidad 111 solo requiere NumPy y ofrece una rama opcional de TensorFlow. `transformers` y un checkpoint español son ampliaciones: las celdas no descargan modelos y funcionan con el baseline local si la carpeta `modelos/nlp/encoder_es_compacto` no existe.

El kit `datos/nlp/` contiene `intents_fase19.json`, `documentos_asistente_fase19.json`, `preguntas_rag_fase19.csv`, sus fichas y la política de modelos opcionales. El proyecto 115 debe ejecutarse sin cuenta cloud ni servicios remotos. En el entorno PyTorch utilizado para validar se instalaron `scikit-learn 1.9.0`, `SciPy 1.18.1`, `Pandas 3.0.5` y `NumPy 2.5.3`; las copias ejecutadas se guardan fuera del repositorio.

## Entorno PyTorch (UT6)

### macOS y Linux

Desde la carpeta raíz del curso, una única vez:

```bash
python3.13 -m venv .venv-pytorch
.venv-pytorch/bin/python -m pip install --upgrade pip
.venv-pytorch/bin/python -m pip install torch torchvision opencv-python-headless matplotlib pandas seaborn jupyterlab ipykernel nbconvert
.venv-pytorch/bin/python -m ipykernel install --user \
  --name curso-pytorch-py313 \
  --display-name "Python 3.13 (PyTorch curso)"
```

Para trabajar posteriormente:

```bash
source .venv-pytorch/bin/activate
jupyter lab
```

### Windows PowerShell

Desde la carpeta raíz del curso, una única vez:

```powershell
py -3.13 -m venv .venv-pytorch
.venv-pytorch\Scripts\python.exe -m pip install --upgrade pip
.venv-pytorch\Scripts\python.exe -m pip install torch torchvision opencv-python-headless matplotlib pandas seaborn jupyterlab ipykernel nbconvert
.venv-pytorch\Scripts\python.exe -m ipykernel install --user --name curso-pytorch-py313 --display-name "Python 3.13 (PyTorch curso)"
```

Para trabajar posteriormente:

```powershell
.venv-pytorch\Scripts\Activate.ps1
jupyter lab
```

Si PowerShell impide activar el entorno, no cambies la política del sistema sin consultar al profesorado; puedes ejecutar las herramientas usando directamente la ruta `.venv-pytorch\Scripts\python.exe`.

### Comprobación obligatoria

Con el entorno PyTorch activado, ejecuta:

```bash
python -c "import sys, torch; print(sys.executable); print(torch.__version__); print(torch.rand(2, 3)); print('CUDA:', torch.cuda.is_available())"
python -m jupyter kernelspec list
```

Debe aparecer una ruta dentro de `.venv-pytorch`, una versión de PyTorch y el kernel `curso-pytorch-py313`. El resultado `CUDA: False` es correcto: las unidades comunes están diseñadas para CPU. Una GPU compatible puede acelerar ampliaciones, pero no es necesaria.

En JupyterLab, abre el cuaderno y usa **Change Kernel** para elegir `Python 3.13 (PyTorch curso)`. Comprueba la primera celda de importación antes de ejecutar el resto.

## Ejecutar una validación completa (profesorado)

Las copias ejecutadas deben escribirse fuera de las carpetas de material para no publicar salidas accidentales:

```bash
mkdir -p /tmp/validacion-pytorch
.venv-pytorch/bin/python -m jupyter nbconvert --to notebook --execute \
  --ExecutePreprocessor.kernel_name=curso-pytorch-py313 \
  --ExecutePreprocessor.timeout=120 \
  --output-dir /tmp/validacion-pytorch \
  unidades/74_tensores_y_calculo_numerico_pytorch.ipynb
```

En Windows se puede sustituir la ruta del intérprete por `.venv-pytorch\Scripts\python.exe` y `/tmp/validacion-pytorch` por una carpeta temporal del usuario. Los cuadernos de alumnado contienen enunciados sin resolver; la solución docente permite comprobar además las aserciones del reto.

## Incidencias frecuentes

1. **Se ejecuta con Python 3.14 o con TensorFlow.** Selecciona el kernel PyTorch; el nombre del kernel es más fiable que el nombre de la aplicación JupyterLab.
2. **`No module named torch`.** El entorno no está activado o PyTorch se instaló en otro intérprete. Ejecuta `python -c "import sys; print(sys.executable)"` y compara la ruta con `.venv-pytorch`.
3. **No aparece el kernel.** Repite `python -m ipykernel install ...` usando el Python de `.venv-pytorch`, no el `python` del sistema.
4. **Falla la instalación de una rueda.** Conserva el mensaje completo, la versión de Python y el sistema operativo. No mezcles paquetes de diferentes entornos; comunica la incidencia para revisar la combinación compatible.
5. **Se intenta usar CUDA, MPS o cámara.** Son ampliaciones opcionales. Vuelve a CPU y a los ejemplos con datos locales para seguir el recorrido común.

## Relación con el entorno inicial

Las primeras unidades se validaron con Python 3.14. El bloque TensorFlow/Keras se trasladó a Python 3.13 en `.venv-tensorflow` y, al comenzar UT6, PyTorch se aisló en `.venv-pytorch`, también con Python 3.13. Esta separación es intencionada y evita modificar el entorno de las unidades ya terminadas. El manual de instalación inicial explica la puesta en marcha de JupyterLab; esta guía añade los cambios necesarios al llegar a UT5 y UT6.

## Fase 20 de UT7 (plataformas, APIs y voz)

Las unidades 116–121 se validan con el kernel `curso-pytorch-py313`, porque reutilizan NumPy, Pandas, OpenCV y los datos locales de NLP. Flask, `boto3` y bibliotecas de audio de proveedores son opcionales: los cuadernos incluyen una implementación local o un doble de contrato cuando no están instalados. Los clips de `datos/nlp/clips_fase20/` son tonos sintéticos de prueba y no contienen habla; no permiten evaluar la precisión de un ASR real.

Para validar el bloque completo sin modificar los cuadernos, guarda las salidas en una carpeta temporal:

```bash
mkdir -p /tmp/validacion-fase20
.venv-pytorch/bin/python -m jupyter nbconvert --to notebook --execute \
  --ExecutePreprocessor.kernel_name=curso-pytorch-py313 \
  --ExecutePreprocessor.timeout=180 \
  --output-dir /tmp/validacion-fase20 \
  unidades/116_nube_plataformas_ia_responsabilidades.ipynb
```

Repite el comando para las unidades 117–120, el proyecto 121 y sus soluciones. Las ramas cloud solo deben activarse con credenciales y autorización explícitas; nunca se incluyen claves en un notebook ni se sube audio real por defecto.

## Fase 21 de UT7 (evaluación, operación y proyecto final)

Las unidades 122–124 y el proyecto 125 reutilizan el kernel `curso-pytorch-py313` y los kits locales de NLP y plataformas. No requieren instalación cloud, Docker, Kubernetes ni una cuenta de pago. El catálogo de proveedores contiene puntuaciones y costes hipotéticos; la captura de configuración y los casos de regresión son sintéticos y están documentados en `datos/plataformas/ficha_fase21.md`.

La validación docente puede guardarse fuera del repositorio:

```bash
mkdir -p /tmp/validacion-fase21
.venv-pytorch/bin/python -m jupyter nbconvert --to notebook --execute \
  --ExecutePreprocessor.kernel_name=curso-pytorch-py313 \
  --ExecutePreprocessor.timeout=180 \
  --output-dir /tmp/validacion-fase21 \
  unidades/122_comparar_plataformas_ia_evidencia.ipynb
```

Repite el comando con 123, 124, el proyecto 125 y sus soluciones. Las comparaciones remotas deben volver a verificarse con documentación fechada, región, límites y autorización; no se incluyen credenciales en los cuadernos.
