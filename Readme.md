# Conector AppSheet

Este proyecto proporciona una interfaz para interactuar con la API de AppSheet, permitiendo realizar acciones como agregar, editar, eliminar y extraer datos de tablas en una aplicación de AppSheet. 

Utiliza Python y la biblioteca `requests` para manejar las solicitudes HTTP.

## Requisitos

- Python 3.12
- Bibliotecas:
  - requests
  - pandas
  - json

Puedes instalar las bibliotecas necesarias utilizando pip:

```python
pip install -r requirements.txt
```

## Estructura del Proyecto

El proyecto contiene los siguientes archivos:

- `configuracion.py`: Contiene la configuración necesaria para conectarse a la API de AppSheet y define la función `enviar_Peticion` para realizar acciones sobre las tablas.
- `funciones.py`: Define la función `conector_AppSheet`, que envía solicitudes a la API utilizando los parámetros especificados.

## Uso

### Configuración Inicial

1. Abre el archivo `configuracion.py`.
2. Reemplaza los valores de `APP_ID` y `APP_ACCESS_KEY` con los correspondientes a tu aplicación en AppSheet.
3. Define el nombre de la tabla en la variable `TABLE_NAME` dentro de tus llamadas a las funciones.

### Ejemplos de Uso

A continuación se presentan ejemplos de cómo utilizar la función `conector_AppSheet` para realizar diferentes acciones:

#### Extraer Datos

Para extraer todos los datos de una tabla:

```python
from funciones import conector_AppSheet
import pandas as pd # Si necesitas manipular DataFrames

datos = conector_AppSheet("F", None, "Actividad")
```


#### Agregar Datos

Para agregar uno o varios registros a la tabla:

```python
df_nuevos_datos = pd.DataFrame({
'ID': [1, 2],
'Nombre': ['Registro 1', 'Registro 2'],
# Otras columnas según tu tabla...
})
conector_AppSheet("A", df_nuevos_datos, "Registros")
```


#### Editar Datos

Para editar uno o varios registros existentes:

```python
df_editar = pd.DataFrame({
'ID': [1],
'Nombre': ['Registro Modificado'],
# Otras columnas a modificar...
})
conector_AppSheet("E", df_editar, "Registros")
```


#### Eliminar Datos

Para eliminar uno o varios registros:

```python
df_eliminar = pd.DataFrame({
'ID': [1],
})
conector_AppSheet("D", df_eliminar, "Registros")
```


## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor abre un issue o envía un pull request.
