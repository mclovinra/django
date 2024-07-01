from django.contrib import admin
from .models import Pedido, DetallePedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id_pedido','rut_cliente'
                    ,'total_pedido']
    list_filter = ['id_pedido','rut_cliente'
                    ,'total_pedido']

@admin.register(DetallePedido)
class DetalleAdmin(admin.ModelAdmin):
    list_display = ['id_pedido','id_producto'
                    ,'precio_producto','cantidad_producto']
    list_filter = ['id_pedido','id_producto'
                    ,'precio_producto','cantidad_producto']