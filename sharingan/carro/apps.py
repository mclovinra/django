from django.apps import AppConfig


class CarroConfig(AppConfig):
    # Define el tipo de campo predeterminado para las claves primarias en los modelos
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Define el nombre de la aplicación
    name = 'carro'
