# Proyecto de ETL para el Balotaje de 2019 en Uruguay

## Descripción General
Este proyecto implementa un proceso de ETL (Extracción, Transformación y Carga) para analizar los datos del balotaje de 2019 en Uruguay. Utiliza Python para extraer datos, realizar transformaciones y cargarlos en una base de datos MySQL.

## Archivos Principales del Proyecto
- **balotage.py**: Maneja la extracción y transformación de los datos del balotaje.
- **base.py**: Incluye funciones para la conexión y operaciones con la base de datos MySQL.
- **constants.py**: Define constantes y configuraciones utilizadas en el proyecto.
- **main.py**: El script principal que ejecuta el flujo completo del proceso ETL.

## Flujo del Proceso ETL
1. **Extracción (E)**: Los datos son extraídos de una fuente online especificada en `constants.py`.
2. **Transformación (T)**: Se aplican transformaciones a los datos.
3. **Carga (L)**: Los datos transformados son cargados en una base de datos MySQL.

## Uso del Archivo .env
El archivo `.env` es necesario para almacenar las credenciales de la base de datos de forma segura. Este archivo debe estar en la raíz del proyecto y no se debe incluir en el control de versiones.

## Instalación de Dependencias
Para instalar las dependencias del proyecto, ejecuta el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```
## Ejecución del Script Principal (main.py)
Para ejecutar el proceso de ETL, sigue estos pasos:
1. Asegúrate de tener instalado Python y MySQL.
2. Instala las dependencias del proyecto con `pip install -r requirements.txt`.
3. Configura el archivo `.env` con las credenciales de tu base de datos MySQL.
4. Ejecuta `main.py` para iniciar el proceso de ETL.

## Contribuciones
Las contribuciones al proyecto son bienvenidas. 


## Autor
- Jean Olmedillo - Autor principal

