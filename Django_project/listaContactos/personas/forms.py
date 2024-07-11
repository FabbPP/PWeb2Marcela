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
    nombres : form.CharField()
    apellidos : form.CharField()
    edad : form.IntegerField()
    signo : form.CharField()
    donador : form.BooleanField()

