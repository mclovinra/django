# tienda/urls.py
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('productos/', views.product_list, name='product_list'),
    path('productos/<int:categoria_id>/', views.product_list, name='product_list_by_category'),
    path('comics/', views.comic_list, name='comic_list'),
    path('producto/<int:id_prod>/', views.product_detail, name='product_detail'),
]