from django.apps import AppConfig


# Configuración de la aplicación 'clientes'
class ClientesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # Campo automático grande por defecto para modelos
    name = 'clientes'  # Nombre de la aplicación
