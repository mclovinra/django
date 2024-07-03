from django.contrib import admin
from .models import Carro, CarroItem

class CarroItemInline(admin.TabularInline):
    model = CarroItem
    extra = 1

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'cliente', 'total_pedido')
    list_display_links = ('id_pedido', 'cliente')
    inlines = [CarroItemInline]

admin.site.register(CarroItem)
