from django.db import models

class Usuario(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    usuario = models.CharField(max_length=100)
    edad = models.BigIntegerField
    password = models.CharField(max_length=254)

class client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=254)  
    class Meta:
        db_table ='cliente'

class producer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=254)   
    class Meta:
        db_table ='productor'


 

class driver(models.Model):
    VEHICLE_TYPE =( 
        ('Pickup', 'Pickup'),
        ('Luv','Luv'),
        ('Turbo', 'Turbo'),
        ('Camion sencillo','Camion'),
        ('Doble troque', 'Doble troque'),
        ('Cuatro manos','Cuatro manos'),
        ('Minimula', 'Minimula'),
        ('Tractomula 2 troques','Tractomula 2 troques'),
        ('Tractomula 3 troques','Tractomula 3 troques'))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    vehicle_type = models.CharField(max_length=254, null=True, choices=VEHICLE_TYPE)
    city = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    password = models.CharField(max_length=254)

    class Meta:
        db_table ='driver'

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)


class tabla_prueba(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    class Meta:
        db_table ='tabla_prueba'

class login(models.Model):
    correo = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=50)
    
    class Meta:
        db_table ='login'

class distribuidor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    identification_card = models.CharField(max_length=10)
    direction =  models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    cell_phone = models.CharField(max_length=11)
    email = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    password = models.CharField(max_length=254)   
    class Meta:
        db_table ='distribuidor'


class registro (models.Model):
    username = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=254)

    class Meta:
        db_table ='registro'

class soporte(models.Model):
    correo = models.CharField(max_length=50)
    comentario = models.CharField(max_length=500)        

    class Meta:
        db_table ='soporte'