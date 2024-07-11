from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from .forms.py import PersonaForm, RawPersonasForm

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
def expOperadoresIf(request):
    categorias = [
        {
            'nombre': 'Frutas',
            'items': ['Manzana', 'Banana', 'Naranja']
        },
        {
            'nombre': 'Verduras',
            'items': ['Lechuga', 'Tomate', 'Zanahoria']
        }
        
    ]
    context = {
        'categorias': categorias,
        'personasRegistradas': personasRegistradas,
    }
    return render(request,"pruebaIf.html",context)
def filtersView (request):
    return render (request,"pruebaFilters.html",{})
def personasTestView (request):
    obj = Persona.objects.get(id = 1)
    context = {
        "nombres": obj.nombres,
        "apellidos": obj.apellidos,
        "edad": obj.edad,
    }
    return render (request,"persona.html", context)
def personasFormView (request):
    form = PersonaForm(request.POST or None)
    if (form.is_valid()):
        form.save()
        form = PersonaForm()
    context = {
        "form" : form
    }
    render (request,./personas/"formPersona.html", context)
def personasFormObjectView(request):
    form = RawPersonasForm(request.POST or None):
    context = {
        "form" : form
    }
    render (request,"formPersona.html"context)