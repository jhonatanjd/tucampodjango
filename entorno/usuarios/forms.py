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