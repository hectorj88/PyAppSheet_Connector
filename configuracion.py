import requests

# Reemplaza con tu App ID y el nombre de la tabla
APP_ID = 'App Id que lo encuentras en las opciones de Integrations' # ID unico de la aplicacion
#TABLE_NAME = 'Actividad'                        # Nombre de la tabla conectada en AppSheet
APP_ACCESS_KEY = 'V2-Application Access Keys'   # KEY generada en APPSHEET para la conexion

# Cabecera de la peticion
headers = {
    "ApplicationAccessKey": APP_ACCESS_KEY,
    "Content-Type": "application/json"
}

def enviar_Peticion(action, rows_data, TABLE_NAME):
    """
    Envía una petición a la API de AppSheet para realizar acciones sobre una tabla.

    Parámetros:
        action (str): La acción a realizar ("A" para agregar, "F" para encontrar,
                      "D" para eliminar, "E" para editar).
        rows_data (list): Los datos a enviar en formato JSON.
        TABLE_NAME: Nombre de la tabla de la base de datos que deseas manipular.

    Retorna:
        dict: Respuesta JSON de la API o None si hubo un error.
    """
    
    url = f"https://www.appsheet.com/api/v2/apps/{APP_ID}/tables/{TABLE_NAME}/Action?applicationAccessKey={APP_ACCESS_KEY}"

    if action not in ["A", "F", "D", "E"] or (action in ["A", "D", "E"] and rows_data is None):
        print("\nLos parámetros especificados son incorrectos\n")
        return None

    body = {
        "Action": action_mapping(action),
        "Properties": {
            "Locale": "en-US",
            "Location": "47.623098, -122.330184",
            "Timezone": "Pacific Standard Time",
        },
        "Rows": rows_data if action != "F" else []
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        print(f"Error en la solicitud: {response.status_code} - {response.text}")
        return None

    return response

def action_mapping(action):
    """Mapea las acciones abreviadas a sus nombres completos."""
    mapping = {
        "A": "Add",
        "F": "Find",
        "D": "Delete",
        "E": "Edit"
    }
    return mapping.get(action)
