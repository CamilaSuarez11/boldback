def parse_json_response(response):
    """Extrae el JSON de la respuesta, manejando errores de forma segura."""
    try:
        return response.json()
    except ValueError:
        raise Exception("Error: Response is not a valid JSON")
