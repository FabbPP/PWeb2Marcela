from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona

def index(request):
    return HttpResponse("Hello, world. You're at the personas index.")
# Create your views here.
personasRegistradas = Persona.objects.all()
def pruebaView(request):
    context = {
    'personasRegistradas': personasRegistradas,
    }
    return render(request, 'prueba.html', context) 
def prueba2View(request):
    context = {
    'personasRegistradas': personasRegistradas,
    }
    return render(request,"base.html",context)

    
