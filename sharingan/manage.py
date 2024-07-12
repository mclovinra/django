#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Establecer la variable de entorno para el archivo de configuración de Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sharingan.settings')
    
    try:
        # Intentar importar la función execute_from_command_line desde django.core.management
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Capturar errores de importación de Django y levantar una excepción más descriptiva
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Ejecutar el comando de línea de comandos de Django con los argumentos proporcionados
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Si este script es ejecutado directamente, llamar a la función main
    main()
