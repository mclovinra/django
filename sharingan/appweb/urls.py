from django.urls import path
from appweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    # Define la URL raíz ('') que apunta a la vista home_view y le asigna el nombre "home"
    path('', views.home_view, name="home"),
    
    # Define otra URL 'home/' que también apunta a la vista home_view
    path('home/', views.home_view),
    
    # path('', views.comic_carrousel, name='home'),
] 

# Agrega la configuración para servir archivos estáticos (como imágenes) en el desarrollo
# Esto permite que los archivos en MEDIA_URL sean accesibles en la ruta document_root definida por MEDIA_ROOT

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)