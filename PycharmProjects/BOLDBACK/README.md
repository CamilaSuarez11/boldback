# Boldback API Testing Project

## Introducción

Este proyecto contiene pruebas automatizadas para interactuar con una API de ejemplo (`reqres.in`). La finalidad del proyecto es validar el comportamiento de la API para diferentes operaciones, como la creación y obtención de usuarios. Las pruebas se estructuran utilizando `pytest` y están organizadas en módulos para facilitar su ejecución y mantenimiento.

Este proyecto debe ejecutarse en un entorno virtual para asegurar que las dependencias sean gestionadas de forma adecuada.

## Requisitos

Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas:

- Python 3.x
- pip (gestor de paquetes de Python)

## Configuración del Entorno Virtual

Para configurar un entorno virtual y activar las dependencias, sigue estos pasos:

1. Crea un entorno virtual:

    ```bash
    python -m venv venv
    ```

2. Activa el entorno virtual:
   - En Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - En macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

## Estructura del Proyecto

```plaintext
.
├── boldback
│   ├── config
│   │   └── settings.py
│   ├── executions
│   │   ├── run_create_user.py
│   │   └── run_get_users_test.py
│   ├── requests
│   │   ├── get_users_request.py
│   │   └── post_create_user_request.py
│   ├── tests
│   │   ├── test_create_user.py
│   │   └── test_get_users.py
│   └── utils
│       └── helpers.py
├── pytest.ini
└── requirements.txt
```

## Archivos Principales

- **config/settings.py**: Contiene la configuración base de la API, como las URLs de los endpoints y el tiempo de espera.
  
- **executions/run_create_user.py** y **executions/run_get_users_test.py**: Archivos de ejecución para correr las pruebas relacionadas con la creación de usuarios y obtención de usuarios, respectivamente.
  
- **requests/get_users_request.py** y **requests/post_create_user_request.py**: Archivos que contienen las funciones que realizan las solicitudes HTTP GET y POST para interactuar con la API.

- **tests/test_create_user.py** y **tests/test_get_users.py**: Archivos de prueba que contienen los test cases que validan las funcionalidades de la API.

- **utils/helpers.py**: Funciones auxiliares para el manejo de respuestas JSON de forma segura.

## Ejecución de Pruebas

Para ejecutar las pruebas, primero asegúrate de que el entorno virtual esté activado y las dependencias estén instaladas.

### Ejecutar Todas las Pruebas

Puedes ejecutar todas las pruebas con el siguiente comando:

```bash
pytest
```

### Ejecutar una Prueba Específica

Si deseas ejecutar una prueba en particular, por ejemplo, las pruebas de creación de usuarios:

```bash
pytest tests/test_create_user.py
```

Las pruebas generarán un reporte que te indicará el estado de cada una de ellas.

## Subir Cambios

Para colaborar y subir tus cambios al repositorio, sigue estos pasos:

1. Haz un fork de este repositorio.
2. Clona tu fork en tu máquina local:

    ```bash
    git clone <url-del-repositorio>
    ```

3. Crea una nueva rama para tus cambios:

    ```bash
    git checkout -b feature/nueva-caracteristica
    ```

4. Realiza los cambios necesarios y añade las pruebas correspondientes.

5. Haz commit de tus cambios:

    ```bash
    git add .
    git commit -m "Descripción de los cambios realizados"
    ```

6. Sube tus cambios a tu repositorio remoto:

    ```bash
    git push origin feature/nueva-caracteristica
    ```

7. Abre un Pull Request en el repositorio original describiendo los cambios que realizaste.

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.
