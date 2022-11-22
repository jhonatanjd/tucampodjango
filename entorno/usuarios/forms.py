from django import forms
#from .models import tabla_prueba, driver, client, producer
from .models import *
#from django.db import models


class add_conductor(forms.ModelForm):
    class Meta:
        model = driver
        fields = '__all__'

class add_usuario(forms.ModelForm):
    class Meta:
        model = client
        fields = '__all__'

class add_productor(forms.ModelForm):
    class Meta:
        model = producer
        fields = '__all__'

class add_prueba(forms.ModelForm):
    class Meta:
        model = tabla_prueba
        fields = '__all__'  

class formato_logeo(forms.ModelForm):
    class Meta:
        model = login
        fields = '__all__'

class otraprueba(forms.ModelForm):
    class Meta:
        model = distribuidor
        fields = '__all__'
        
class form_registro(forms.ModelForm):
    class Meta:
        model = registro
        fields = '__all__'


class form_soporte(forms.ModelForm):
    class Meta:
        model = soporte
        fields = '__all__'

                              