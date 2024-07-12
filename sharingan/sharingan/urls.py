"""
URL configuration for sharingan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appweb import views

# Configuración de las URLs del proyecto Django
urlpatterns = [
    # Ruta para acceder al panel de administración de Django
    path('admin/', admin.site.urls),

    # URLs de la aplicación 'tienda'
    path('tienda/', include('tienda.urls')),

    # Ruta de la página de inicio del sitio, usando la vista 'home_view' y con nombre 'home'
    path('', views.home_view, name='home'),

    # URLs de la aplicación 'appweb'
    path('appweb/', include('appweb.urls')),

    # URLs de la aplicación 'clientes'
    path('clientes/', include('clientes.urls')),

    # URLs de la aplicación 'carro'
    path('carro/', include('carro.urls')),
]

# Configuración para servir archivos estáticos (media) durante el desarrollo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)