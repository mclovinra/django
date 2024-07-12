from django.contrib.auth.backends import BaseBackend
from .models import Cliente

# Backend personalizado para autenticar clientes
class ClienteBackend(BaseBackend):
    # Método para autenticar usuarios basado en el Rut y contraseña
    def authenticate(request, rut_cli=None, password=None, **kwargs):
        try:
            # Intenta obtener un cliente con el Rut proporcionado
            user = Cliente.objects.get(rut_cli=rut_cli)

            # Verifica si la contraseña proporcionada coincide con la contraseña almacenada del cliente
            if user.check_password(password):
                return user  # Retorna el cliente si la autenticación es exitosa
            else:
                return None  # Retorna None si la contraseña no coincide
        except Cliente.DoesNotExist:
            return None  # Retorna None si no se encuentra ningún cliente con el Rut proporcionado

    # Método para obtener un usuario por su ID
    def get_user(self, user_id):
        try:
            # Intenta obtener un cliente por su ID
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None  # Retorna None si no se encuentra ningún cliente con el ID proporcionado
