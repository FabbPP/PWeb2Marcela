from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("formObject/", views.personasFormObjectView, name='personas_form_object'),
    path("form/", views.personasFormView, name='personas_form_object'),
]