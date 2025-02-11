import requests
from boldback.config.settings import Config

def create_user_request(nombre, trabajo):
    """
    Realiza una solicitud POST para crear un usuario.

    Args:
        nombre (str): Nombre del usuario.
        trabajo (str): Trabajo del usuario.

    Returns:
        response: Objeto de respuesta de la solicitud HTTP.
    """
    url = f"{Config.BASE_URL}{Config.POST_CREATE_USER_URL}"
    payload = {}

    if nombre:
        payload["nombre"] = nombre
    if trabajo:
        payload["trabajo"] = trabajo

    response = requests.post(url, json=payload, timeout=Config.TIMEOUT)

    return response
