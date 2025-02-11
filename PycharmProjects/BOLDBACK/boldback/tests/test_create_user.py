import pytest
import datetime
from boldback.requests.post_create_user_request import create_user_request
from boldback.config.settings import Config


def get_current_time_utc():
    """Retorna la fecha y hora actual en formato UTC"""
    return datetime.datetime.utcnow().isoformat() + "Z"


@pytest.mark.parametrize(
    "nombre,trabajo,expected_status_code,expected_response",
    [
        ("morfeo", "líder", 201, {"nombre": "morfeo", "trabajo": "líder"}),

        ("morfeo", None, 201, {"nombre": "morfeo"}),

        (None, "líder", 201, {"trabajo": "líder"}),

        (None, None, 201, {"id": "735"}),  # El ID es dinámico
    ]
)
def test_create_user(nombre, trabajo, expected_status_code, expected_response):
    response = create_user_request(nombre, trabajo)

    assert response.status_code == expected_status_code

    if expected_status_code == 201:
        assert "id" in response.json()

        assert isinstance(response.json().get("id"), str)  # El ID debe ser un string

        created_at = response.json().get("createdAt")
        expected_time = get_current_time_utc()

        created_at_trimmed = created_at[:19]  # Recortar a los primeros 19 caracteres
        expected_time_trimmed = expected_time[:19]  # Recortar a los primeros 19 caracteres

        assert created_at_trimmed == expected_time_trimmed  # Comparamos solo la parte de la fecha y hora

        if expected_response.get("nombre"):
            assert response.json().get("nombre") == expected_response.get("nombre")
        if expected_response.get("trabajo"):
            assert response.json().get("trabajo") == expected_response.get("trabajo")
    else:
        assert "error" in response.json()
