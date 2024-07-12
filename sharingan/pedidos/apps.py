from django.apps import AppConfig


class PedidosConfig(AppConfig):
    # Define the configuration for the 'pedidos' Django application.

    # Specify the default auto-generated primary key field for models in this app.
    default_auto_field = 'django.db.models.BigAutoField'

    # Set the name of the application to 'pedidos'.
    name = 'pedidos'
