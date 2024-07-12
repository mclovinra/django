# carro/views.py
from django.shortcuts import render
from tienda.models import Producto, Categoria, CategoriaProd

def home_view(request):
    cart_count = 0  # Inicializa la variable del conteo del carrito a 0
    
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Lógica para obtener la cantidad de artículos en el carrito
        cart_count = 0  # Reemplaza con tu lógica para contar los artículos en el carrito

    # Obtiene una lista de los primeros 12 productos del tipo 'Comic' que tienen stock disponible
    comics_list = Producto.objects.filter(tipo_prod='Comic', stock_prod__gte=1)[:12]
    
    # Obtiene una lista de los primeros 12 productos del tipo 'Manga' que tienen stock disponible
    mangas_list = Producto.objects.filter(tipo_prod='Manga', stock_prod__gte=1)[:12]

    # Crea el contexto para pasar a la plantilla
    context = {
        'cart_count': cart_count,  # Conteo de artículos en el carrito
        'comics': comics_list,  # Lista de cómics disponibles
        'mangas': mangas_list,  # Lista de mangas disponibles
    }
    
    # Renderiza la plantilla 'home.html' con el contexto proporcionado
    return render(request, 'home.html', context)

def cart_view(request):
    cart_items = []  # Inicializa la lista de artículos en el carrito vacía
    
    # Crea el contexto para pasar a la plantilla
    context = {
        'cart_items': cart_items,  # Lista de artículos en el carrito
    }



# def comic_carrousel(request):
#     comics_list = Producto.objects.filter(tipo_prod='Comic', stock_prod__gte=15)
#     print(comics_list)
#     return render(request, 'home.html', {'comics': comics_list})