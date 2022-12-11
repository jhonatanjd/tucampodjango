from pyexpat import model
from django.db import models
from .choices import *


class registro (models.Model):
    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)
    #rol = models.CharField(max_length=254, choices=ROL)
    nombres = models.CharField(max_length=254)
    apellidos = models.CharField(max_length=254)
    cedula = models.CharField(max_length=254)
    direcion = models.CharField(max_length=254)
    telefono = models.CharField(max_length=254)
    celular = models.CharField(max_length=254)
    correo = models.CharField(max_length=254)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)

    class Meta:
        db_table ='registro'

    def __str__(self):
        return self.username      

class soporte(models.Model):
    correo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)        

    class Meta:
        db_table ='soporte'

class inventario (models.Model):
    producto = models.CharField(max_length=254,choices=PRODUCTS_FRUTAS)
    cantidad = models.CharField(max_length=254, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=254)
    precio_total = models.CharField(max_length=254)
    ciudad = models.CharField(max_length=254, choices=CIUDADS)
    fecha_disponible = models.CharField(max_length=254)
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=254, choices=ESTADO)

    class Meta:
        db_table ='inventario'

    def __str__(self):
        return self.producto                               

class productos (models.Model):
    producto = models.CharField(max_length=254,choices=PRODUCTS_FRUTAS)
    cantidad = models.CharField(max_length=254, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=254)
    precio_total = models.CharField(max_length=254)
    ciudad = models.CharField(max_length=254, choices=CIUDADS)
    fecha_disponible = models.CharField(max_length=254)
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=254, choices=ESTADO)

    class Meta:
        db_table ='productos'

    def __str__(self):
        return self.producto 

class vehiculo (models.Model):
    tipo_vehiculo = models.CharField(max_length=100,choices=TIPO_VEHICULO, )
    tipo_carroceria = models.CharField(max_length=100, choices=TIPO_CARROCERIA)
    capacidad = models.CharField(max_length=100, choices=CAPACIDAD)
    marca = models.CharField(max_length=254,choices=MARCA)
    modelo= models.CharField(max_length=4)
    placa= models.CharField(max_length=6,unique=True)
    color = models.CharField(max_length=100, choices=COLOR)

    class Meta:
        db_table ='vehiculo'

    def __str__(self):
        return self.tipo_vehiculo 

class cliente(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=9, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.CharField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    class Meta:
        db_table ='cliente'

    def __str__(self):
            return self.nombres
    
class productor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=9, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.CharField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    class Meta:
        db_table ='productor'

    def __str__(self):
            return self.nombres
    
class conductor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=9, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.CharField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    
    class Meta:
        db_table ='conductor'

    def __str__(self):
            return self.nombres



