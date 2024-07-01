from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria, CategoriaProd

def product_list(request, categoria_id=None):
    categorias = Categoria.objects.all()

    if categoria_id:
        categoria = get_object_or_404(Categoria, id=categoria_id)
        # Obtener los IDs de productos asociados a la categoría seleccionada
        ids_productos = CategoriaProd.objects.filter(id_catego=categoria_id).values_list('id_produc', flat=True)
        # Filtrar productos por los IDs obtenidos y por stock mayor a 0
        productos = Producto.objects.filter(id_prod__in=ids_productos, stock_prod__gt=0)
    else:
        categoria = None
        # Filtrar todos los productos por stock mayor a 0
        productos = Producto.objects.filter(stock_prod__gt=0)

    return render(request,
                  'productos/list.html',
                  {'categoria': categoria,
                   'categorias': categorias,
                   'productos': productos})
