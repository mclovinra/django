"""
WSGI config for sharingan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Establece la variable de entorno DJANGO_SETTINGS_MODULE con el módulo de configuración de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharingan.settings')

# Obtiene la aplicación WSGI para este proyecto Django
application = get_wsgi_application()