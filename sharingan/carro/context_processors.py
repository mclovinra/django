from .models import Carro
from django.contrib.auth.models import User

def cart_count(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'username'):
            cart_count = 0  # No se cuenta ningún carrito para el usuario root
        else:
            # Lógica para usuarios normales
            try:
                cliente = request.user.rut_cli  # Obtiene el objeto Cliente asociado al usuario
                carro, created = Carro.objects.get_or_create(cliente_id=cliente)  # Obtiene o crea un carrito para el cliente
                cart_count = carro.items.count() 
            except Carro.DoesNotExist:
                cart_count = 0
    else:
        cart_count = 0
    return {'cart_count': cart_count}
