from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    # Ruta para agregar un producto al carrito
    # La URL contiene el ID del producto (producto_id) como un entero
    path('add/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),

    # Ruta para ver el detalle del carrito
    path('cart/', views.cart_detail, name='cart_detail'),

    # Ruta para actualizar el carrito
    # Esta ruta probablemente maneja una solicitud POST para actualizar las cantidades de los items en el carrito
    path('update_cart/', views.update_cart, name='update_cart'),

    # Ruta para crear un pedido desde el carrito
    # La URL contiene el ID del carrito (carro_id) como un entero
    path('crear-pedido/<int:carro_id>/', views.crear_pedido_desde_carro, name='crear_pedido_desde_carro'),
]
