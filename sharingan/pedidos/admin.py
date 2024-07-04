from django.contrib import admin
from .models import Pedido, DetallePedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id_pedido', 'cliente', 'total_pedido']
    list_filter = ['id_pedido', 'cliente__rut_cli', 'total_pedido']

@admin.register(DetallePedido)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'precio_unitario', 'cantidad']
    list_filter = ['pedido__id_pedido', 'producto', 'precio_unitario', 'cantidad']