from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Persona
from .forms import PersonaForm, RawPersonaForm

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
    return render (request,"personas/formPersona.html", context)
def personasFormObjectView(request):
    if request.method == 'POST':
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombres']  # Change 'nombre' to 'nombres'
            apellidos = form.cleaned_data['apellidos']
            edad = form.cleaned_data['edad']
            signo = form.cleaned_data['signo']
            donador = form.cleaned_data.get('donador', False)  # Use .get to avoid KeyError

            # Do something with the data, for example, save it to the database

            return redirect('success_url')  # Redirect after POST

    else:
        form = RawPersonaForm()
    context =  {
        "form" : form
    }
    return render (request,"personas/formPersona.html",context)