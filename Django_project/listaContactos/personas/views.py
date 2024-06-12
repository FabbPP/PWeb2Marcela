from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from django.template import loader

def index(request):
    return HttpResponse("Hello, world. You're at the personas index.")
# Create your views here.
personasRegistradas= Persona.objects.all()
def pruebaView(request):
    #template = loader.get_template('prueba.html')
    context = {
    'personasRegistradas': personasRegistradas,
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'prueba.html', context) 

    
