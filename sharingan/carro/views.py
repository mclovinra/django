# carro/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from tienda.models import Producto
from django.contrib.auth.decorators import login_required
from .models import Carro, CarroItem
from clientes.models import Cliente

def home_view(request):
    cart_count = 0
    if request.user.is_authenticated:
        # Lógica para obtener la cantidad de artículos en el carrito
        cart_count = 0  # Reemplaza con tu lógica para contar los artículos en el carrito

    context = {
        'cart_count': cart_count,
    }
    return render(request, 'home.html', context)


@login_required
def cart_detail(request):
    # Obtener el usuario autenticado
    user = request.user

    # Verificar si el usuario tiene un cliente asociado
    if hasattr(user, 'rut_cli'):
        cliente = user.rut_cli  # Acceder al cliente asociado mediante la relación OneToOneField
        carro = get_object_or_404(Carro, cliente=cliente)

        context = {
            'carro': carro,
        }
        return render(request, 'carro/cart_detail.html', context)
    else:
        # Manejar el caso donde el usuario no tiene un cliente asociado
        return render(request, 'carro/cart_detail.html', {})


@login_required
def add_to_cart(request, producto_id):
    producto = get_object_or_404(Producto, id_prod=producto_id)
    user = request.user

    if hasattr(user, 'rut_cli'):
        cliente = user.rut_cli

        # Verificar si hay stock disponible para el producto
        if producto.stock_prod > 0:
            # Obtener o crear el carro del cliente
            carro, created = Carro.objects.get_or_create(cliente=cliente)

            # Verificar si el producto ya está en el carro
            carro_item, item_created = CarroItem.objects.get_or_create(carro=carro, producto=producto)

            print(f'{carro_item.quantity} - {producto.stock_prod}')
            
            if not item_created:
                if carro_item.quantity < producto.stock_prod:
                    carro_item.quantity += 1
                    carro_item.save()
                    carro.update_total()
                    messages.success(request, f"{producto.titulo_prod} se ha agregado al carrito.")
                else:
                    messages.warning(request, f"No se pueden agregar más unidades de {producto.titulo_prod} al carrito.")
            else:
                carro.update_total()
                messages.success(request, f"{producto.titulo_prod} se ha agregado al carrito.")

            # Redirigir al detalle del producto agregado al carrito
            return redirect('product_detail', id_prod=producto_id)
        else:
            messages.error(request, f"No hay stock disponible para {producto.titulo_prod}.")
    else:
        messages.error(request, "Debe iniciar sesión para agregar productos al carrito.")

    return redirect('product_detail', id_prod=producto_id)


def update_cart(request):
    if request.method == 'POST':
        carro_id = request.POST.get('carro_id')
        
        try:
            carro = Carro.objects.get(id_pedido=carro_id)
            carro_items = CarroItem.objects.filter(carro=carro)

        except Carro.DoesNotExist:
            messages.error(request, f'No se encontró un carro con ID {carro_id}.')
            return redirect('carro:cart_detail')

        for item in carro_items:
            item_id = item.id
            quantity = request.POST.get(f'item_{item_id}_quantity')

            if quantity is not None:
                action = request.POST.get(f'action', '')
                if action == f'resta_{item_id}':
                    # Si se presionó el botón de resta para este ítem
                    item.quantity -= 1
                elif action == f'suma_{item_id}':
                    # Si se presionó el botón de suma para este ítem
                    # Verificar si la cantidad en el carro ya iguala al stock disponible
                    if item.quantity < item.producto.stock_prod:
                        item.quantity += 1
                    else:
                        messages.warning(request, f"No se pueden agregar más unidades de {item.producto.titulo_prod} al carrito.")
                else:
                    # Si no se presionó ningún botón de suma o resta, mantener la cantidad actual
                    pass

                if item.quantity <= 0:
                    item.delete()  # Eliminar el ítem si la cantidad es 0 o menor
                else:
                    item.save()  # Guardar el ítem actualizado

        carro.update_total()
        messages.success(request, 'Carro actualizado correctamente.')
        return redirect('carro:cart_detail')
    
    else:
        messages.error(request, 'Método no permitido.')
        return redirect('carro:cart_detail')
