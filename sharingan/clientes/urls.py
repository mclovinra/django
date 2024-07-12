# cliente/urls.py

from django.urls import path
from .views import registro_view, login_view, logout_view

urlpatterns = [
    # URL para la vista de registro
    path('registro/', registro_view, name='registro'),
    
    # URL para la vista de inicio de sesión
    path('login/', login_view, name='login'),
    
    # URL para la vista de cierre de sesión
    path('logout/', logout_view, name='logout'),
]