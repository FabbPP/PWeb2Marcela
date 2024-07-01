from django.contrib import admin
from django.urls import include,path
from inicio.views import myHomeView
from inicio.views import anotherView
from personas.views import pruebaView
from personas.views import prueba2View
from personas.views import expOperadoresIf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('personas.urls')),
    path('', myHomeView, name = "Pagina de Inicio"),
    path('another/', anotherView),
    path('pruebaTags/', pruebaView),
    path('pruebaTags2/', prueba2View),
    path ('pruebaIf/', expOperadoresIf) ,
]
