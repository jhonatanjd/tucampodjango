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
class form_registro_frutas(forms.ModelForm):
    class Meta:
        model = frutas
        fields = '__all__'  

class form_registro_verduras(forms.ModelForm):
    class Meta:
        model = verduras
        fields = '__all__'

class form_registro_leguminosas(forms.ModelForm):
    class Meta:
        model = leguminosas
        fields = '__all__'

class form_registro_granos(forms.ModelForm):
    class Meta:
        model = granos
        fields = '__all__'

class form_registro_carnes(forms.ModelForm):
    class Meta:
        model = carnes
        fields = '__all__'       

class form_registro_abarrotes(forms.ModelForm):
    class Meta:
        model = abarrotes
        fields = '__all__'       

class form_registro_lacteos(forms.ModelForm):
    class Meta:
        model = lacteos
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
        model = Productor
        fields = '__all__'

class form_vehiculo(forms.ModelForm):
    class Meta:
        model = vehiculo
        fields = '__all__'           

                              