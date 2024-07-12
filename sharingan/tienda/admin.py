from django.contrib import admin
from .models import Categoria, Producto, CategoriaProd

# Admin para la categoría
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_cat', 'desc_cat']  # Campos que se mostrarán en la lista de categorías
    # Filtros disponibles en la interfaz de administración para categorías
    list_filter = ['id_cat', 'desc_cat']

# Admin para el producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id_prod', 'titulo_prod', 'volumen_prod', 'desc_prod', 'precio_prod', 'stock_prod', 'editorial_prod', 'tipo_prod']
    # Filtros disponibles en la interfaz de administración para productos
    list_filter = ['id_prod', 'titulo_prod', 'desc_prod', 'editorial_prod']
    # Campos editables directamente desde la lista de productos en la interfaz de administración
    list_editable = ['precio_prod', 'stock_prod', 'tipo_prod']

# Admin para la relación entre categorías y productos
@admin.register(CategoriaProd)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id_catego', 'id_produc']  # Campos que se mostrarán en la lista de relaciones
    # Filtros disponibles en la interfaz de administración para la relación entre categorías y productos
    list_filter = ['id_catego', 'id_produc']
