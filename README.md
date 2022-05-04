
# Crear el entorno virtual
- virtualenv venv

# Activar el ambiente virtual
- source venv/bin/activate

# Instalar las frameworks / librerías
Recordemos que para realizar instalación de cualquier librería en Python, podemos hacerlo mediante el comando pip install <LIBRERIA> en este caso vamos a instalar las siguientes librerías

- pip install django djangorestframework djangorestframework-simplejwt 
- pip install django-model-utils

El siguiente paso es crear un nuevo proyecto de Django

- django-admin startproject "NOMBRE DEL PROJECTO"

Asegúrate que todo funcione hasta aquí. Puedes probar la ejecución del servidor Django con el siguiente comando:

- python manage.py runserver

# Instalación y configuración de Django REST Framework

Para instalar el Djago Rest Framework ejecutar el siguiente comando en la consola

- pip install djangorestframework

Después de instalar el framework debemos realizar la siguiente configuración, en el archivo settings.py vamos a agregar la aplicación rest_framework en la sección INSTALLED_APPS

INSTALLED_APPS = [
    ...
    'rest_framework',
]
Si tienes alguna duda del proceso de instalación puedes consultar la documentación oficial: https://www.django-rest-framework.org/

# Crear aplicación
Ahora vamos a crear una aplicación

- python manage.py startapp "nombre de la aplicación"

Registre la aplicación  en el proyecto, esto lo puedes hacer mediante el archivo settings.py del proyecto

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    **'example'**
]
4. Crear migraciones

# Crear una migración

- python manage.py makemigrations

# Correr todas las migraciones

- python manage.py migrate

# Crear un acceso al admin de Django

- python manage.py createsuperuser

