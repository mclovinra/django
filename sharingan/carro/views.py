# carro/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from tienda.models import Producto
from django.contrib.auth.decorators import login_required
from .models import Carro, CarroItem
from clientes.models import Cliente
from pedidos.models import Pedido 

def home_view(request):
    cart_count = 0  # Inicializa la variable del conteo del carrito a 0
    if request.user.is_authenticated:  # Verifica si el usuario está autenticado
        cart_count = 0  # Lógica para obtener la cantidad de artículos en el carrito (aquí aún no implementada)

    context = {
        'cart_count': cart_count,  # Conteo de artículos en el carrito
    }
    return render(request, 'home.html', context)  # Renderiza la plantilla 'home.html' con el contexto proporcionado


@login_required
def cart_detail(request):
    user = request.user  # Obtiene el usuario actual

    if hasattr(user, 'rut_cli'):  # Verifica si el usuario tiene un atributo 'rut_cli'
        cliente = user.rut_cli  # Obtiene el 'rut_cli' del usuario
        carro, created = Carro.objects.get_or_create(cliente_id=cliente)  # Obtiene o crea un carrito para el cliente

        context = {
            'carro': carro,  # Pasa el carrito al contexto
        }
        return render(request, 'carro/cart_detail.html', context)  # Renderiza la plantilla con el contexto
    else:
        return render(request, 'carro/cart_detail.html', {})  # Si el usuario no tiene 'rut_cli', renderiza la plantilla vacía


@login_required
def add_to_cart(request, producto_id):
    producto = get_object_or_404(Producto, id_prod=producto_id)  # Obtiene el producto o retorna un 404 si no existe
    user = request.user  # Obtiene el usuario actual

    if hasattr(user, 'rut_cli'):  # Verifica si el usuario tiene un atributo 'rut_cli'
        cliente = user.rut_cli  # Obtiene el 'rut_cli' del usuario

        if producto.stock_prod > 0:  # Verifica si hay stock del producto
            carro, created = Carro.objects.get_or_create(cliente_id=cliente)  # Obtiene o crea un carrito para el cliente

            # Obtiene o crea un item en el carrito para el producto
            carro_item, item_created = CarroItem.objects.get_or_create(carro=carro, producto=producto)

            if not item_created:  # Si el item ya existía
                if carro_item.quantity < producto.stock_prod:
                    carro_item.quantity += 1  # Incrementa la cantidad del item en el carrito
                    carro_item.save()  # Guarda el item
                    carro.update_total()  # Actualiza el total del carrito
                    messages.success(request, f"{producto.titulo_prod} se ha agregado al carrito.")
                else:
                    messages.warning(request, f"No se pueden agregar más unidades de {producto.titulo_prod} al carrito.")
            else:
                carro.update_total()  # Actualiza el total del carrito si el item fue creado
                messages.success(request, f"{producto.titulo_prod} se ha agregado al carrito.")

            return redirect('product_detail', id_prod=producto_id)  # Redirige a la página de detalle del producto
        else:
            messages.error(request, f"No hay stock disponible para {producto.titulo_prod}.")
    else:
        messages.error(request, "Debe iniciar sesión para agregar productos al carrito.")

    return redirect('product_detail', id_prod=producto_id)  # Redirige a la página de detalle del producto en caso de error


def update_cart(request):
    if request.method == 'POST':
        carro_id = request.POST.get('carro_id')  # Obtiene el ID del carrito desde el POST

        try:
            carro = Carro.objects.get(id_pedido=carro_id)  # Obtiene el carrito por ID
            carro_items = CarroItem.objects.filter(carro=carro)  # Obtiene todos los items del carrito

        except Carro.DoesNotExist:
            messages.error(request, f'No se encontró un carro con ID {carro_id}.')
            return redirect('carro:cart_detail')

        for item in carro_items:  # Itera sobre los items del carrito
            item_id = item.id
            quantity = request.POST.get(f'item_{item_id}_quantity')  # Obtiene la cantidad deseada del POST

            if quantity is not None:
                action = request.POST.get(f'action', '')
                if action == f'resta_{item_id}':
                    item.quantity -= 1  # Resta 1 a la cantidad del item
                elif action == f'suma_{item_id}':
                    if item.quantity < item.producto.stock_prod:
                        item.quantity += 1  # Suma 1 a la cantidad del item si hay suficiente stock
                    else:
                        messages.warning(request, f"No se pueden agregar más unidades de {item.producto.titulo_prod} al carrito.")
                else:
                    pass

                if item.quantity <= 0:
                    item.delete()  # Elimina el item si la cantidad es 0 o menor
                else:
                    item.save()  # Guarda los cambios en el item

        carro.update_total()  # Actualiza el total del carrito
        messages.success(request, 'Carro actualizado correctamente.')
        return redirect('carro:cart_detail')  # Redirige a la vista del detalle del carrito

    else:
        messages.error(request, 'Método no permitido.')
        return redirect('carro:cart_detail')  # Redirige a la vista del detalle del carrito en caso de error


def crear_pedido_desde_carro(request, carro_id):
    carro = get_object_or_404(Carro, id_pedido=carro_id)  # Obtiene el carrito o retorna un 404 si no existe

    if request.method == 'GET':

        for item in carro.items.all():  # Itera sobre los items del carrito
            producto = Producto.objects.get(id_prod=item.producto.id_prod)  # Obtiene el producto asociado al item

            if item.quantity > producto.stock_prod:
                messages.error(request, f"Stock insuficiente para el producto {producto.titulo_prod}")
                return redirect('carro:cart_detail')  # Redirige a la vista del detalle del carrito en caso de stock insuficiente

        pedido = Pedido.crear_desde_carro(carro)  # Crea un pedido desde el carrito
        
        return redirect('carro:cart_detail')  # Redirige a la vista del detalle del carrito
    
    return redirect('carro:cart_detail')  # Redirige a la vista del detalle del carrito en caso de error