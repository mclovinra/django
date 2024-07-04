# carro/views.py
from django.shortcuts import render
from tienda.models import Producto, Categoria, CategoriaProd

def home_view(request):
    cart_count = 0
    if request.user.is_authenticated:
        # Lógica para obtener la cantidad de artículos en el carrito
        cart_count = 0  # Reemplaza con tu lógica para contar los artículos en el carrito

    comics_list = Producto.objects.filter(tipo_prod='Comic', stock_prod__gte=15)[:12]

    context = {
        'cart_count': cart_count,
        'comics': comics_list,
    }
    return render(request, 'home.html', context)

def cart_view(request):
    cart_items = []
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)

# def comic_carrousel(request):
#     comics_list = Producto.objects.filter(tipo_prod='Comic', stock_prod__gte=15)
#     print(comics_list)
#     return render(request, 'home.html', {'comics': comics_list})