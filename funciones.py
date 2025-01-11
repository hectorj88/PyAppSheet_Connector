
import json  # Importar json para convertir el cuerpo a string
from configuracion import enviar_Peticion, action_mapping
from pandas import json_normalize
#pip freeze > requirements.txt #Codigo para ejecutar en la consola y obtener las dependencias


def conector_AppSheet(action, df, TABLE_NAME):
    """
    Envía una petición a la API de AppSheet para realizar la acciones como la de eliminar, agregar, editar o extraer datos sobre una tabla.

    Parámetros:
        action (str): La acción a realizar ("A" para agregar, "F" para Extraer los datos,
                      "D" para eliminar, "E" para editar).
        df: Se requiere el Dataframe que desea agregar, debe tener las mismas variable que la tabla destino,
            debe contener el el ID del registro del dato para asi saber cual modificar, no se requiere cuando la accion es extraer los datos.
        TABLE_NAME: Nombre de la tabla de la base de datos que deseas manipular.

    Retorna:
        JSON cuando la eliminacion de datos fue exitosa   

    Ejemplos:
        Para extraer todos los datos de la tabla
            Datos = conector_AppSheet("F", None, "Actividad")
        
        Para Eliminar uno o varios datos de la tabla
            conector_AppSheet("D", df, "Actividad") # df debe contener al menos el ID del o los registros a eliminar
            
        Para editar uno o varios datos de la tabla
            Datos = conector_AppSheet("E", df, "Actividad") # df debe contener al menos el ID del o los registros a eliminar y las varibles a editar

        Para agregar uno o varios datos de la tabla
            Datos = conector_AppSheet("A", df, "Actividad") # df debe contener el ID unico del o los registros a agregar y las varibles
    """

    # Realiza la solicitud POST a la API
    if action=="F":
        response = enviar_Peticion(action, None, TABLE_NAME)
    else:
        # Convertir el DataFrame a una lista de diccionarios
        rows_data = df.to_dict(orient='records')
        response = enviar_Peticion(action, rows_data, TABLE_NAME)

    # Verifica el estado de la respuesta
    if response.status_code == 200:
        try:
            # Extrae los datos en formato JSON y los transforma en el dataframe
            data = json_normalize(response.json())
            print(f"La accion de {action_mapping(action)} fue realizada sobre los siguientes datos:\n", data.to_json(),"\n")
            if data.empty:
                print("No se encontraron datos en la tabla\n")
            if action=="F":
                return data            
        except json.JSONDecodeError:
            print("Error al decodificar JSON:", response.text)
    else:
        print("Error al obtener los datos:", response.status_code)
        print("Contenido de la respuesta:", response.text)
