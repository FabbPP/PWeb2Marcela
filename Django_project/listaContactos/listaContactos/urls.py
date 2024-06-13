from django.contrib import admin
from django.urls import include,path
from inicio.views import myHomeView
from inicio.views import anotherView
from personas.views import pruebaView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', include('personas.urls')),
    path('', myHomeView, name = "Pagina de Inicio"),
    path('another/', anotherView),
    path('pruebaTags/', pruebaView),
]
