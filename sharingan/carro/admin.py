from django.contrib import admin
from .models import Carro, CarroItem

class CarroItemInline(admin.TabularInline):
    # Especifica el modelo que se utilizará para la relación en línea
    model = CarroItem
    # Define el número de formularios extra vacíos a mostrar
    extra = 1

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    # Define los campos que se mostrarán en la lista de la vista de administración
    list_display = ('id_pedido', 'cliente', 'total_pedido')
    # Define los campos que serán enlaces en la lista de la vista de administración
    list_display_links = ('id_pedido', 'cliente')
    # Especifica las relaciones en línea a mostrar en el formulario de detalles del modelo
    inlines = [CarroItemInline]

# Registra el modelo CarroItem en la vista de administración
admin.site.register(CarroItem)
