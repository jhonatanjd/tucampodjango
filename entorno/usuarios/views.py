from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from usuarios.forms import *
from usuarios.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import frutas
from usuarios.models import frutas
def Home (request):
    return render(request, 'home.html')

def frutas1 (request):
    return render(request, 'frutas.html')

def verduras1 (request):
    return render(request, 'verduras.html')   

def granos1 (request):
    return render(request, 'granos.html')

def leguminosas1 (request):
    return render(request, 'leguminosas.html')

def carnes1 (request):
    return render(request, 'carnes.html')     

def abarrotes1 (request):
    return render(request, 'abarrotes.html')

def lacteos1 (request):
    return render(request, 'lacteos.html')

def l_lacteos (request):
    lacteo=lacteos.objects.all()
    l={'lacteo':lacteo}

    return render(request, 'listas_lacteos.html',l)

def l_abarrotes (request):
    abarrote=abarrotes.objects.all()
    w={'abarrote':abarrote}
    return render(request, 'listas_abarrotes.html',w)

def l_carnes (request):
    carne=carnes.objects.all()
    a={'carne':carne}
    return render(request, 'listas_carnes.html',a)

def l_leguminosas (request):
    leguminosa=leguminosas.objects.all()
    e={'leguminosa':leguminosa}
    return render(request, 'listas_leguminosas.html',e)

def l_granos (request):
    grano=granos.objects.all()
    s={'grano':grano}
    return render(request, 'listas_granos.html',s)

def l_verduras (request):
    verdura=verduras.objects.all()
    q={'verdura':verdura}
    return render(request, 'listas_verduras.html',q)

def l_frutas (request):
    fruta=frutas.objects.all()
    r={'fruta':fruta}
    return render(request, 'l_frutas.html',r) 
    
def vender (request):
    if "seguridad" in request.session:
        return render(request, 'vender.html')
    else:
        return render(request, 'logueo_productor.html')      
        
def comprar (request):
    return render(request, 'comprar.html') 

def quien (request):
    return render(request, 'quienesSomos.html')

def productor1 (request):
    fruta= frutas.objects.all()
    r={'fruta':fruta}

    vehiculos=vehiculo.objects.all()
    data= {'vehiculos':vehiculos}
    return render(request, 'productor.html',r)           

def l_pescados (request):
    return render(request, 'l_pescados.html') 

def cliente1 (request):
    return render(request, 'cliente.html')

def conductor1 (request):
    vehiculos=vehiculo.objects.all()
    data= {'vehiculos':vehiculos}
    return render(request, 'conductor.html',data)
def ofertas (request):
    return render(request, 'ofertas.html')

def ayuda (request):
    return render(request, 'ayuda.html')

def rol (request):
    return render(request, 'rol.html') 
def rol_registro (request):
    return render(request, 'rol_registro.html') 
         
def registro_cliente(request):
    if request.method == 'POST':
        form = add_cliente(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = form.cleaned_data['username']
            var.password =make_password(form.cleaned_data['password'])
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
        form = add_cliente ()
    return render (request,"registrar_usuario.html",{'form': form})

def registro_productor(request):
    if request.method == 'POST':
        form = add_productor(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = form.cleaned_data['username']
            var.password =make_password(form.cleaned_data['password'])
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
        form = add_productor ()
    return render (request,"registrar_productor.html",{'form': form})

def registro_conductor(request):
    if request.method == 'POST':
        form = add_conductor(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = form.cleaned_data['username']
            var.password =make_password(form.cleaned_data['password'])
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
        form = add_conductor ()
    return render (request,"registrar_conductor.html",{'form': form})

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

def logueo_cliente (request):
    return render (request, 'logueo_cliente.html') 

def logueo_productor (request):
    return render (request, 'logueo_productor.html') 

def logueo_conductor (request):
    return render (request, 'logueo_conductor.html') 

def validacion_cliente(request):
    if request.method == 'POST':
        user=request.POST.get('username')
        passw=request.POST.get('password')

        if cliente.objects.filter(username=user).exists():
            logueo=cliente.objects.get(username=user)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo_cliente.html')
            else:
                request.session['seguridad']=True
                return render (request, 'cliente.html')
        else: 
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_cliente.html')            
    
def validacion_productor (request):
    
    if request.method == 'POST':
        user=request.POST.get('username')
        passw=request.POST.get('password')
        
        if Productor.objects.filter(username=user).exists():
            logueo=Productor.objects.get(username=user)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo_productor.html')
            else:
                request.session['seguridad']=True
                return render (request,'vender.html')

        else:
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_productor.html')

def validacion_conductor (request):
    
    if request.method == 'POST':
        user=request.POST.get('username')
        passw=request.POST.get('password')
        
        if conductor.objects.filter(username=user).exists():
            logueo=conductor.objects.get(username=user)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo_conductor.html')
            else:
                request.session['seguridad']=True
                return render (request,'conductor.html')

        else:
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_conductor.html')

def salir (request):
    del request.session['seguridad']
    return render(request,'rol.html')

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

#def vender (request):
    return render(request,'vender.html')

def registro_vehiculo (request):
    if request.method == 'POST':
        form = form_vehiculo(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.tipo_vehiculo = form.cleaned_data['tipo_vehiculo']
            var.tipo_carroceria = form.cleaned_data['tipo_carroceria']
            var.capacidad = form.cleaned_data['capacidad']
            var.marca = form.cleaned_data['marca']
            var.modelo = form.cleaned_data['modelo']
            var.placa = form.cleaned_data['placa']
            var.color = form.cleaned_data['color']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_vehiculo() 
    return render (request,'registrar_vehiculo.html',{'form': form})
        
def clase_producto(request):
    return render(request,'clase_producto.html')
                 
def buscador(request):
    if request.GET["prd"]:
        #mensaje="articulo buscado: %r" %request.GET["prd"]
        busqueda=request.GET["prd"]
        if len(busqueda)>25:
            mensaje="texto de busqueda demasiado largo"
        else:    
            prod=productos.objects.filter(nombre__icontains=busqueda)
            return render(request, "resultados_busqueda.html", {"productos":prod, "query":busqueda})
    else:
        mensaje="no has introducido nada"
        return HttpResponse(mensaje) 
                 
def validacion_manual (request):
    if request.method == 'POST':
        user=request.POST.get('username')
        passw=request.POST.get('password')
        print(user)
        print(passw)
        if registro.objects.filter(username=user).exists():
            logueo=registro.objects.get(username=user)
            passw=check_password(passw,logueo.password)
            if passw ==False:
                messages.error(request,'usuario o contraseña erronea')
                return render(request,'logueo_productor.html')               
            else:
                request.session['seguridad'] = True
                return render (request,'productor.html')
        else:
            messages.error(request,'usuario o contraseña erronena')
            return render(request,'logueo_productor.html')
               
def registro_frutas (request):
    if request.method == 'POST':
        form = form_registro_frutas(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_frutas() 
    return render (request,'registro_frutas.html',{'form': form})
    
def registro_verduras (request):
    if request.method == 'POST':
        form = form_registro_verduras(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_verduras() 
    return render (request,'registro_verduras.html',{'form': form})

def registro_leguminosas (request):
    if request.method == 'POST':
        form = form_registro_leguminosas(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_leguminosas() 
    return render (request,'registro_leguminosas.html',{'form': form})    

def registro_granos (request):
    if request.method == 'POST':
        form = form_registro_granos(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_granos() 
    return render (request,'registro_granos.html',{'form': form})

def registro_carnes (request):
    if request.method == 'POST':
        form = form_registro_carnes(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_carnes() 
    return render (request,'registro_carnes.html',{'form': form})

def registro_abarrotes (request):
    if request.method == 'POST':
        form = form_registro_abarrotes(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_abarrotes() 
    return render (request,'registro_abarrotes.html',{'form': form})

def registro_lacteos (request):
    if request.method == 'POST':
        form = form_registro_lacteos(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.prodducto = form.cleaned_data['producto']
            var.cantidad = form.cleaned_data['cantidad']
            var.precio_kgs = form.cleaned_data['precio_kgs']
            var.precio_total = form.cleaned_data['precio_total']
            #var.fecha_disponible = form.cleaned_data['fecha_disponible']
            var.ofrece_transporte = form.cleaned_data['ofrece_transporte']
            var.descripcion = form.cleaned_data['descripcion']
            var.estado = form.cleaned_data['estado']
            var.save()
            messages.success(request,'producto cargado!!!')
        else:
         messages.warning(request,'producto no cargado')
    else:
        form = form_registro_lacteos() 
    return render (request,'registro_lacteos.html',{'form': form})