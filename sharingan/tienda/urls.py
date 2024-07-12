# tienda/urls.py
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    # Ruta para listar todos los productos
    path('productos/', views.product_list, name='product_list'),

    # Ruta para listar productos por categoría específica
    path('productos/<int:categoria_id>/', views.product_list, name='product_list_by_category'),

    # Ruta para listar todos los productos de tipo 'Comic'
    path('comics/', views.comic_list, name='comic_list'),

    # Ruta para listar todos los productos de tipo 'Manga'
    path('mangas/', views.manga_list, name='manga_list'),

    # Ruta para ver el detalle de un producto específico por su id_prod
    path('producto/<int:id_prod>/', views.product_detail, name='product_detail'),

    # Ruta para realizar búsquedas de productos por título
    path('productos/buscar/', views.search_results, name='search'),
]