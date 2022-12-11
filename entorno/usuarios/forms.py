from django import forms
from .models import *
#from django.forms import ModelForm
#from .models import tabla_prueba, driver, client, producer
#from django.db import model
#from django.forms import ModelForm


    
class form_registro(forms.ModelForm):
    class Meta:
        model = registro
        fields = '__all__'

class form_soporte(forms.ModelForm):
    class Meta:
        model = soporte
        fields = '__all__'

class form_registro_productos(forms.ModelForm):
    class Meta:
        model = productos
        fields = '__all__' 
class form_registro_productos(forms.ModelForm):
    class Meta:
        model = inventario
        fields = '__all__'    

class add_conductor(forms.ModelForm):
    class Meta:
        model = conductor
        fields = '__all__'

class add_cliente(forms.ModelForm):
    class Meta:
        model = cliente
        fields = '__all__'

class add_productor(forms.ModelForm):
    class Meta:
        model = productor
        fields = '__all__'

class form_vehiculo(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = '__all__'           

                              