from django.contrib.auth.backends import BaseBackend
from .models import Cliente

class ClienteBackend(BaseBackend):
    def authenticate(request, rut_cli=None, password=None, **kwargs):
        try:
            user = Cliente.objects.get(rut_cli=rut_cli)
            print(f"auth - {password}")
            if user.check_password(password):
                return user
            else:
                return None
        except Cliente.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Cliente.objects.get(pk=user_id)
        except Cliente.DoesNotExist:
            return None
