
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')), #puxando as urls isoladas para cá
    path('', include('usuarios.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Passa para o django que ele precisa utilizar as variáveis que criamos no settings
