from .models import Carro

def cart_count(request):
    if request.user.is_authenticated:
        try:
            cliente = request.user.rut_cli  # Obtiene el 'rut_cli' del usuario
            carro, created = Carro.objects.get_or_create(cliente_id=cliente)  # Obtiene o crea un carrito para el cliente
            cart_count = carro.items.count() 
        except Carro.DoesNotExist:
            cart_count = 0
    else:
        cart_count = 0
    return {'cart_count': cart_count}
