from django.shortcuts import render
from django.http import HttpResponse
from personas.models import Persona
personasRegistradas = Persona.objects.all()
# Create your views here.
def myHomeView(request,*args, **kwargs):
    print(args,kwargs)
    print(request.user)
    context = {
        'personasRegistradas': personasRegistradas
    }
    return render(request,"home.html",context)
def anotherView(request):
    return HttpResponse("<h1>Hola, solo otra pagina</h1>")
