"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
#from miapp import views
import miapp.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola-mundo/',miapp.views.hola_mundo,name='hola-mundo'),
    path('hola-mundo/<int:redirigir>/',miapp.views.hola_mundo,name='hola-mundo'),
    path('',miapp.views.index,name='pagina-principal'),
    path('bucle-while/',miapp.views.bucle_while,name='bucle-while'),
    path('contacto/',miapp.views.contacto,name='contacto'),
    path('contacto/<str:nombre>/',miapp.views.contacto,name='contacto'),
    path('contacto/<str:nombre>/<str:apellidos>',miapp.views.contacto,name='contacto'),
    path('crear-articulo/<str:title>/<str:content>/<str:public>',miapp.views.crear_articulo,name='crear_articulo'),
    path('articulo/',miapp.views.articulo,name='articulo'),
    path('editar-articulo/<int:id>',miapp.views.editar_articulo,name='editar-articulo'),
    path('articulos/',miapp.views.articulos,name='articulos'),
    path('borrar-articulo/<int:id>',miapp.views.borrararticulo,name='borrar-articulo'),
    path('save-article/',miapp.views.save_article,name='save-article'),
    path('create_article/',miapp.views.create_article,name='create-article'),
    path('create-full-article/',miapp.views.create_full_article,name='create_full'),
]

#Configuracion para cargar imagenes

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

