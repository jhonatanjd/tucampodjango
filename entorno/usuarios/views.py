from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from usuarios.forms import *
from usuarios.models import *

def Home (request):
    return render(request, 'home.html')

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
    return render(request, 'leguminosas.html')

def l_granos (request):
    return render(request, 'listas_granos.html')

def l_verduras (request):
    return render(request, 'listas_verduras.html')

def l_frutas (request):
    return render(request, 'l_frutas.html')    

def vender (request):
    return render(request, 'vender.html')        
def comprar (request):
    return render(request, 'comprar.html') 


def quien (request):
    return render(request, 'quienesSomos.html')

def productor (request):
    return render(request, 'productor.html')           

def cliente (request):
    return render(request, 'cliente.html')

def conductor (request):
    return render(request, 'conductor.html')

def ofertas (request):
    return render(request, 'ofertas.html')

def ayuda (request):
    return render(request, 'ayuda.html')

def compra (request):
    return render(request, 'compra.html')   

def login_usu (request):
    return render(request, 'login_usuarios.html') 

def login_cond (request):
    return render(request, 'login_conductor.html') 

def registro_manual(request):
    return render(request,'registrar_usuario_manual.html')

def agregar_usuario(request):
    if request.method == 'POST':
        form = add_usuario(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.nombre = form.cleaned_data['first_name']
            var.apellido = form.cleaned_data['last_name']
            var.cedula = form.cleaned_data['identification_card']
            var.direccion = form.cleaned_data['direction']
            var.telefono = form.cleaned_data['phone']
            var.celular = form.cleaned_data['cell_phone']
            var.email = form.cleaned_data['email']
            var.ciudad = form.cleaned_data['city']
            var.password =make_password(form.cleaned_data['password'])
            var.save()
            messages.success(request,'usuario cargado exitosamente!!!')
        else:
         messages.warning(request,'Usuario no cargado')
    else:
        form = add_usuario()
    return render (request,"registrar_usuario_manual.html",{'form': form})
            

def agregar_cond(request):
    if request.method == 'POST':
        form = add_conductor(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.nombre = form.cleaned_data['first_name']
            var.apellido = form.cleaned_data['last_name']
            var.cedula = form.cleaned_data['identification_card']
            var.direccion = form.cleaned_data['direction']
            var.telefono = form.cleaned_data['phone']
            var.celular = form.cleaned_data['cell_phone']
            var.email = form.cleaned_data['email']
            var.tipo_vehiculo = form.cleaned_data['vehicle_type']
            var.ciudad = form.cleaned_data['city']
            var.edad = form.cleaned_data['year']
            var.password =make_password(form.cleaned_data['password'])
            var.save()
            messages.success(request,'usuario cragado exitosamente!!!')
        else:
         messages.warning(request,'Usuario no cargado')
    else:
        form=add_conductor()
    return render (request,"registrar_conductor.html",{'form': form})

def add_usuario1 (request):
    if request.method == 'POST':
        nom=request.POST.get("firts_name")
        apell=request.POST.get("last_name")
        ide=request.POST.get("identification_card")
        dir=request.POST.get("direction")
        phone=request.POST.get("phone")
        cell=request.POST.get("cell_phone")
        email=request.POST.get("email")
        veh=request.POST.get("vehicle_type")
        city=request.POST.get("city")
        year=request.POST.get("year")
        passw=request.POST.get("password")
        passw= make_password("passw")
        p=driver(first_name=nom, last_name=apell, identification_card=ide, direction=dir, phone=phone, cell_phone=cell, email=email, 
        vehicle_type=veh, city=city, year=year, password=passw)
        p.save()       
    messages.success(request,'usuario registrado exitosamente !!!')
    return render (request,"crear_usuario.html")
