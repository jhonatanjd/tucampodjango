from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from usuarios.forms import *
from usuarios.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def Home (request):
    return render(request, 'home.html')

def Home1 (request):
    return render(request, 'home1.html')    

def frutas (request):
    return render(request, 'frutas.html')

def verduras (request):
    return render(request, 'verduras.html')   

def granos (request):
    return render(request, 'granos.html')

def leguminosas (request):
    return render(request, 'leguminosas.html')

def carnes (request):
    return render(request, 'carnes.html')     

def abarrotes (request):
    return render(request, 'abarrotes.html')

def lacteos (request):
    return render(request, 'lacteos.html')

def l_lacteos (request):
    return render(request, 'listas_lacteos.html')

def l_abarrotes (request):
    return render(request, 'listas_abarrotes.html')

def l_carnes (request):
    return render(request, 'listas_carnes.html')

def l_leguminosas (request):
    return render(request, 'listas_leguminosas.html')

def l_granos (request):
    return render(request, 'listas_granos.html')

def l_verduras (request):
    return render(request, 'listas_verduras.html')

def l_frutas (request):
    return render(request, 'l_frutas.html') 

#@login_required
def vender (request):
    if "seguridad" in request.session:
        return render(request, 'vender.html')
    else:
        return render(request, 'logueo_manual.html')      
#@login_required         
def comprar (request):
    return render(request, 'comprar.html') 

def quien (request):
    return render(request, 'quienesSomos.html')

def productor (request):
    return render(request, 'productor.html')           


def l_pescados (request):
    return render(request, 'l_pescados.html') 


def cliente (request):
    return render(request, 'cliente.html')

def conductor (request):
    return render(request, 'conductor.html')

def ofertas (request):
    return render(request, 'ofertas.html')

def ayuda (request):
    return render(request, 'ayuda.html')

def login_usu (request):
    return render(request, 'login_usuarios.html') 

def login_cond (request):
    return render(request, 'login_conductor.html') 

def registro_manual(request):
    return render(request,'registrar_usuario_manual.html')


           
def logueo_exitosos (request):
    if "seguridad" in request.session:
        return render (request, 'logueo_exitosos.html')
    else:
         return render(request, 'logueo_manual.html')   

def registro_func(request):
    if request.method == 'POST':
        form = form_registro(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = form.cleaned_data['username']
            var.password =make_password(form.cleaned_data['password'])
            var.rol = form.cleaned_data['rol']
            var.nombres = form.cleaned_data['nombres']
            var.apellidos = form.cleaned_data['apellidos']
            var.cedula = form.cleaned_data['cedula']
            var.direccion = form.cleaned_data['direcion']
            var.telefono = form.cleaned_data['telefono']
            var.celular = form.cleaned_data['celular']
            var.correo = form.cleaned_data['correo']
            var.ciudad = form.cleaned_data['ciudad']
            var.save()
            messages.success(request,'usuario cargado exitosamente!!!')
        else:
         messages.warning(request,'Usuario no cargado')
    else:
        form = form_registro ()
    return render (request,"registro.html",{'form': form})

def soporte (request):
    if request.method == 'POST':
        form = form_soporte(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.correo = form.cleaned_data['correo']
            var.comentario = form.cleaned_data['comentario'] 
            var.save()
            messages.success(request,'comentario cargado!!!')
        else:
         messages.warning(request,'Usuario no cargado')
    else:
        form = form_soporte() 
    return render (request,"ayuda.html",{'form': form})

#def login (request):
    return render(request, 'registration/login.html') 

def logueo_manual (request):
    return render (request, 'logueo_manual.html') 

def validacion_manual (request):
    if request.method == 'POST':
        user=request.POST.get('email')
        passw=request.POST.get('password')
        print(user)
        print(passw)
        if registro.objects.filter(username=user).exists():
            logueo=registro.objects.get(username=user)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo_manual.html')
            else:
                request.session['seguridad']=True
                return render (request,'logueo_exitosos.html')

        else:
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_manual.html')

def salir (request):
    del request.session['seguridad']
    return render(request,'logueo_manual.html')

def registro_productos (request):
    if request.method == 'POST':
        form = form_registro_productos(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_productos() 
    return render (request,'registrar_productos.html',{'form': form})

                    
def list_tusproductos (request):
    if "seguridad" in request.session:
    
        return render (request, 'tus_productos.html')
    else:
        return render (request, 'logueo_manual.html') 
        
def clase_producto(request):
    return render(request,'clase_producto.html')
                 
def listas (request):
    return render(request, 'lista.html')                  
