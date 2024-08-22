# Django REST API para Autores y Libros

Este proyecto es una API RESTful construida con Django y Django REST Framework para gestionar información sobre autores y libros. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los recursos de Autor y Libro.

## Características

- **Operaciones CRUD**:
  - **Autores**: Crear, leer, actualizar y eliminar autores.
  - **Libros**: Crear, leer, actualizar y eliminar libros.
- **Serialización**: Uso de serializadores para convertir instancias de Django en datos JSON.

## Endpoints

### Autores

- `GET /autores/` - Listar todos los autores.
- `GET /autores/{id}/` - Obtener un autor específico por ID.
- `POST /autores/` - Crear un nuevo autor.
- `PUT /autores/{id}/` - Actualizar un autor existente.
- `DELETE /autores/{id}/` - Eliminar un autor.

### Libros

- `GET /libros/` - Listar todos los libros.
- `GET /libros/{id}/` - Obtener un libro específico por ID.
- `POST /libros/` - Crear un nuevo libro.
- `PUT /libros/{id}/` - Actualizar un libro existente.
- `DELETE /libros/{id}/` - Eliminar un libro.

## Documentación de la API

Toda la documentación de la API, incluyendo ejemplos de solicitudes y respuestas para cada endpoint, está disponible en Postman. Puedes acceder a ella en el siguiente enlace:

[Documentación de la API en Postman](https://documenter.getpostman.com/view/10308727/2sAXjDdvAS#81e6edad-d93a-4bc3-a6b5-b38c45f03f83)


## Requisitos

- Python 3.12.5
- Django 5.1
- Django REST Framework

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/JaimeHere/autocom_django_rest_api.git
    cd autocom_django_rest_api
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv virtual_env
    source virtual_env/bin/activate
    pip install -r requirements.txt
    ```

3. Modifica la conexión a la base de datos, en el archivo settings.py usando tus datos locales. 
    ```python
   DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.postgresql",
            'NAME': 'your_database_name',
            'USER': 'your_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
    ```
**Nota: En este proyecto no se aseguraron los datos de conexión de forma intencionada.**
    
4. Configura las migraciones y aplica las migraciones iniciales:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Uso

Puedes interactuar con la API utilizando herramientas como [Postman](https://www.postman.com/) o `curl`. Por ejemplo, para listar todos los autores:

```bash
curl -X GET http://127.0.0.1:8000/autores/