from django.urls import path
from .views import add_to_cart, cart_detail, update_cart

app_name = 'carro'

urlpatterns = [
    path('add/<int:producto_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('update_cart/', update_cart, name='update_cart'),

]
