# tienda/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.product_list, name='product_list'),
    path('productos/<int:categoria_id>/', views.product_list, name='product_list_by_category'),
    path('comics/', views.comic_list, name='comic_list'),
]
