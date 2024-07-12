#!/usr/bin/env bash

# Establecer la opción para que el script falle si hay algún error
set -o errexit

# Instalar las dependencias listadas en el archivo requirements.txt usando pip
pip install -r requirements.txt

# Recolectar los archivos estáticos de la aplicación
python manage.py collectstatic --noinput

# Aplicar todas las migraciones pendientes en la base de datos
python manage.py migrate

# Ejecutar el servidor usando Gunicorn para manejar las peticiones HTTP
exec gunicorn sharingan.wsgi:application --bind 0.0.0.0:$PORT --workers 3