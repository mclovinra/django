# carro/views.py
from django.shortcuts import render

def home_view(request):
    cart_count = 0
    if request.user.is_authenticated:
        # Lógica para obtener la cantidad de artículos en el carrito
        cart_count = 0  # Reemplaza con tu lógica para contar los artículos en el carrito

    context = {
        'cart_count': cart_count,
    }
    return render(request, 'home.html', context)

def cart_view(request):
    cart_items = []
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)
