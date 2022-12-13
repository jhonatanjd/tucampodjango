
from django.contrib import admin
from django.urls import path
from usuarios.views import *
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',Home, name="home"),
    path('frutas/',frutas1, name="frutas"),
    path('verduras/',verduras1, name="verduras"),
    path('granos/',granos1, name="granos"),
    path('leguminosas/',leguminosas1, name="leguminosas"),
    path('granos/',granos1, name="granos"),
    path('carnes/',carnes1, name="carnes"),
    path('abarrotes/',abarrotes1, name="abarrotes"),
    path('lacteos/',lacteos1, name="lacteos"),
    path('l_lacteos/',l_lacteos, name="l_lacteos"),
    path('l_abarrotes/',l_abarrotes, name="l_abarrotes"),
    path('l_carnes/',l_carnes, name="l_carnes"),
    path('l_leguminosas/',l_leguminosas, name="l_leguminosas"),
    path('l_granos/',l_granos, name="l_granos"),
    path('l_verduras/',l_verduras, name="l_verduras"),
    path('l_frutas/',l_frutas, name="l_frutas"),
    path('vender/',vender, name="vender"),
    path('comprar/',comprar, name="comprar"),
    path('quien/',quien, name="quien"),
    path('productor/',productor1, name="productor"),
    path('cliente/',cliente1, name="cliente"),
    path('conductor/',conductor1, name="conductor"),
    path('ofertas/',ofertas , name="ofertas"),
    path('ayuda/',ayuda, name="ayuda"),
    
    path('validacion_cliente/',validacion_cliente, name="validacion_cliente"),
    path('validacion_productor/',validacion_productor, name="validacion_productor"),
    path('validacion_conductor/',validacion_conductor, name="validacion_conductor"),
    path('logueo_cliente/',logueo_cliente, name="logueo_cliente"),
    path('logueo_productor/',logueo_productor, name="logueo_productor"),
    path('logueo_conductor/',logueo_conductor, name="logueo_conductor"),
    path('registro_cliente/',registro_cliente, name="registro_cliente"),
    path('registro_productor/',registro_productor, name="registro_productor"),
    path('registro_conductor/',registro_conductor, name="registro_conductor"),
    path('registro_vehiculo/',registro_vehiculo, name="registro_vehiculo"),
    path('registro_frutas/',registro_frutas, name="registro_frutas"),
    path('registro_verduras/',registro_verduras, name="registro_verduras"),
    path('registro_leguminosas/',registro_leguminosas, name="registro_leguminosas"),
    path('registro_granos/',registro_granos, name="registro_granos"),
    path('registro_carnes/',registro_carnes, name="registro_carnes"),
    path('registro_abarrotes/',registro_abarrotes, name="registro_abarrotes"),
    path('registro_lacteos/',registro_lacteos, name="registro_lacteos"),
    
    
    path('validacion_manual/',validacion_manual, name="validacion_manual"),
    
    
    path('soporte/',soporte, name="soporte"),
    path('salir/',salir, name="salir"),
    path('buscador/',buscador, name="buscador"),
    path('registro_productos/',registro_productos, name="registro_productos"),
    
   
    path('clase_producto/',clase_producto, name="clase_producto"),
    path('l_pescados/',l_pescados, name="l_pescados"),
    path('rol/',rol, name="rol"),
    path('rol_registro/',rol_registro, name="rol_registro"),
    ]       
