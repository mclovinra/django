from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, CategoriaProd

def product_list(request, categoria_id=None):
    # Obtener todas las categorías disponibles
    categorias = Categoria.objects.all()

    if categoria_id:
        # Si se proporciona una categoria_id, obtener la categoría correspondiente o mostrar error 404
        categoria = get_object_or_404(Categoria, id=categoria_id)
        # Obtener los IDs de productos asociados a la categoría seleccionada
        ids_productos = CategoriaProd.objects.filter(id_catego=categoria_id).values_list('id_produc', flat=True)
        # Filtrar productos por los IDs obtenidos y por stock mayor a 0
        productos = Producto.objects.filter(id_prod__in=ids_productos, stock_prod__gt=0)
    else:
        # Si no se proporciona una categoria_id, establecer categoria como None
        categoria = None
        # Filtrar todos los productos por stock mayor a 0
        productos = Producto.objects.filter(stock_prod__gt=0)

    # Renderizar la plantilla 'productos/list.html' con los datos de categoría, categorías y productos
    return render(request,
                  'productos/list.html',
                  {'categoria': categoria,
                   'categorias': categorias,
                   'productos': productos})

def comic_list(request):
    # Filtrar productos de tipo 'Comic'
    productos = Producto.objects.filter(tipo_prod='Comic')
    
    # Renderizar la plantilla 'productos/comics.html' con los productos filtrados
    return render(request, 'productos/comics.html', {'productos': productos})

def manga_list(request):
    # Filtrar productos de tipo 'Manga'
    productos = Producto.objects.filter(tipo_prod='Manga')
    
    # Renderizar la plantilla 'productos/mangas.html' con los productos filtrados
    return render(request, 'productos/mangas.html', {'productos': productos})

def product_detail(request, id_prod):
    # Obtener un producto específico por su id_prod o mostrar error 404 si no existe
    producto = get_object_or_404(Producto, id_prod=id_prod)
    
    # Renderizar la plantilla 'productos/product_detail.html' con el detalle del producto obtenido
    return render(request, 'productos/product_detail.html', {'producto': producto})

def search_results(request):
    # Obtener el parámetro 'q' de la consulta GET
    query = request.GET.get('q')
    
    if query:
        # Si hay un valor en 'q', filtrar productos por título que contenga la cadena de consulta
        productos = Producto.objects.filter(titulo_prod__icontains=query)
    else:
        # Si no hay consulta, devolver un conjunto vacío de productos
        productos = Producto.objects.none()
    
    # Renderizar la plantilla 'productos/search_results.html' con los productos filtrados y la cadena de consulta
    return render(request, 'productos/search_results.html', {'productos': productos, 'query': query})