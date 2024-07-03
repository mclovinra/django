from django.urls import path
from appweb import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [    
    path('', views.home_view, name="home"),
    path('home/', views.home_view),   
] 

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)