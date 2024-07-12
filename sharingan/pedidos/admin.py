from django.contrib import admin
from .models import Pedido, DetallePedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    # Admin configuration for the Pedido model.

    # Display these fields in the list view of the admin interface.
    list_display = ['id_pedido', 'cliente', 'total_pedido']

    # Add filters to the admin interface for these fields.
    list_filter = ['id_pedido', 'cliente__rut_cli', 'total_pedido']

@admin.register(DetallePedido)
class DetalleAdmin(admin.ModelAdmin):
    # Admin configuration for the DetallePedido model.

    # Display these fields in the list view of the admin interface.
    list_display = ['pedido', 'producto', 'precio_unitario', 'cantidad']

    # Add filters to the admin interface for these fields.
    list_filter = ['pedido__id_pedido', 'producto', 'precio_unitario', 'cantidad']