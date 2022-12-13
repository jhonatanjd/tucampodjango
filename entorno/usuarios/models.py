from pyexpat import model
from django.db import models
from .choices import *


class registro (models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    #rol = models.CharField(max_length=254, choices=ROL)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=9, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.CharField(max_length=100, unique=True)
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

class cliente(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    #correo = models.CharField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    class Meta:
        db_table ='cliente'

    def __str__(self):
            return self.nombres
    
class Productor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    #correo = models.CharField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS)  
    class Meta:
        db_table ='productor'

    def __str__(self):
            return self.nombres

class frutas (models.Model):
    producto = models.CharField(max_length=100,choices=PRODUCTS_FRUTAS)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='frutas'

    def __str__(self):
        return self.producto 

class verduras (models.Model):
    producto = models.CharField(max_length=100,choices=VERDURAS_LIST)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='verduras'

    def __str__(self):
        return self.producto 

class leguminosas (models.Model):
    producto = models.CharField(max_length=100,choices=LEGUMINOSAS_LIST)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='leguminosas'

    def __str__(self):
        return self.producto 

class granos (models.Model):
    producto = models.CharField(max_length=100,choices=GRANOS_LIST)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='granos'

    def __str__(self):
        return self.producto        

class carnes (models.Model):
    producto = models.CharField(max_length=100,choices=CARNES_LIST)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='carnes'

    def __str__(self):
        return self.producto          

class abarrotes (models.Model):
    producto = models.CharField(max_length=100,choices=ABARROTES_LIST)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='abarrotes'

    def __str__(self):
        return self.producto

class lacteos (models.Model):
    producto = models.CharField(max_length=100,choices=LACTEOS_LIST)
    cantidad = models.CharField(max_length=100, choices=CANTIDAS)
    precio_kgs = models.CharField(max_length=100)
    precio_total = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50, choices=CIUDADS)
    #fecha_disponible = models.DateField(verbose_name='fecha disponible')
    #fecha_disponible = models.CharField(verbose_name='fecha disponible')
    ofrece_transporte = models.CharField(max_length=254, choices=SI_NO)
    descripcion = models.CharField(max_length=254)
    estado = models.CharField(max_length=50, choices=ESTADO)

    class Meta:
        db_table ='lacteos'

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
    #conductor= models.ForeignKey (conductor, null=True, blank=True,on_delete=models.CASCADE)
                    
    class Meta:
        db_table ='vehiculo'
                
        def __str__(self):
            return self.placa
                        
class conductor (models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True) 
    direcion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    celular = models.CharField(max_length=10, unique=True)
    #correo = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(max_length=100, unique=True)
    ciudad= models.CharField(max_length=40, choices=CIUDADS) 
    #vehiculo= models.ForeignKey (vehiculo, null=True, blank=True,on_delete=models.CASCADE)
                        
    class Meta:
        db_table ='conductor'
                    
        def __str__(self):
            return self.username 
