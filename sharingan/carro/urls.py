from django.urls import path
from . import views

app_name = 'carro'

urlpatterns = [
    path('add/<int:producto_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('update_cart/', views.update_cart, name='update_cart'),
    path('crear-pedido/<int:carro_id>/', views.crear_pedido_desde_carro, name='crear_pedido_desde_carro'),

]
