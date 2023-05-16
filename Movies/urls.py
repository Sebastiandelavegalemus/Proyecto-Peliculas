from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from webapp.views import home, peliculas_por_categoria, pelicula_detalle

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('home/', home)
    path('', home),
    path('<int:categoria_id>', peliculas_por_categoria, name='peliculas_por_categoria'),
    path('detalle/<int:pelicula_id>', pelicula_detalle, name='pelicula_detalle')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#Recibiendo un entero