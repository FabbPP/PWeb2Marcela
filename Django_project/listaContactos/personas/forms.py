from django import forms
from .models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            "nombres",
            "apellidos",
            "edad",
            "signo",
            "donador"
        ]
#forms objeto#
class RawPersonaForm(forms.Form):
    nombres = forms.CharField()
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    signo = forms.CharField()
    donador = forms.BooleanField()

