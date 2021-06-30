from django.shortcuts import render, redirect, get_object_or_404
from .models import Mercancia, Usuario
from django import forms
from .forms import MercanciaForm
from .forms import UsuarioForm
from django.contrib import messages

# Create your views here.
def home(request):
    mercancia = Mercancia.objects.all()
    datos = {
        'mercancia':mercancia
    }
    return render(request, 'xartgord/index.html', datos)

def personajes(request):
    return render(request, 'xartgord/personajes.html')

def items(request):
    return render(request, 'xartgord/items.html')

def enemigos(request):
    return render(request, 'xartgord/enemigos.html')

def contact(request):
    return render(request, 'xartgord/contact.html')

def mercancia(request):
    return render(request, 'xartgord/mercancia.html')

def armas(request):
    return render(request, 'xartgord/armas.html')

def armaduras(request):
    return render(request, 'xartgord/armaduras.html')

def objetos(request):
    return render(request, 'xartgord/objetos.html')

def cuenta(request):
    return render(request, 'xartgord/cuenta.html')

def polerones(request):
    return render(request, 'xartgord/polerones.html')

def usuario(request):
    return render(request, 'xartgord/usuario.html')

def registro(request):
    return render(request, 'xartgord/registro.html')

def form_mod_usuario(request):
    return render(request, 'xartgord/form_mod_usuario.html')

def form_usuario(request):
    return render(request, 'xartgord/form_usuario.html')
def listas(request):
    return render(request, 'xartgord/listas.html')

def form_mercancia(request):

    mercancia = Mercancia.objects.all()
    datos = {
        'mercancia':mercancia,
        'form':MercanciaForm()
    }
    if (request.method == 'POST'):
        formulario=MercanciaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos Guardados correctamente'
        else:
            formulario=MercanciaForm()
            datos['mensaje'] = 'ERROR: no se puedo guardar el producto, intentelo mas tarde'
    return render(request, 'xartgord/form_mercancia.html',datos) 

def form_modifimerca(request, id):
    mercancia = Mercancia.objects.get(idproducto=id)
    datos = {
        'form':MercanciaForm(instance=mercancia)
    }
    if(request.method == 'POST'):
        formulario = MercanciaForm(request.POST, request.FILES, instance=mercancia)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Modificado correctamente'
        else:
            formulario=MercanciaForm()
            datos['mensaje'] = 'ERROR: no se puedo guardar el producto, intentelo mas tarde'
    return render(request, 'xartgord/form_modifimerca.html',datos)  

##eliminar
def form_eliminar(request, id):
    mercancia = Mercancia.objects.get(idproducto=id)
    mercancia.delete()
    
    return redirect(to='form_mercancia')
#agregar polerones


#LISTA DE USUARIOS 
def usuarios(request):
    listausuarios = Usuario.objects.raw('SELECT * FROM Usuario order by Rut') 
    datos = {
        'usuarios':listausuarios
    }
    return render(request, 'xartgord/usuario.html', datos) 

#REGISTRAR USUARIO
def form_reg_usuario(request):
    datos = {
        'form':UsuarioForm()
    }
    if(request.method == 'POST'): #post guardar datos
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
        else:
            formulario = UsuarioForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'xartgord/usuario.html',datos)

#post registrar datos usuario
def registro(request):
    datos = {
        'form':UsuarioForm()
    }
    if(request.method == 'POST'):
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Registrado correctamente'
        else:
            formulario = UsuarioForm()
            datos['mensaje'] = 'ERROR: No se ha registrado, intente nuevamente'
    return render(request,'xartgord/registro.html',datos)

#MODIFICAR USUARIO
def form_mod_usuario(request,id):
    usuario = Usuario.objects.get(Rut = id)
    datos = {
        'form':UsuarioForm(instance=usuario)
    }
    
    if(request.method == 'POST'): #post guardar datos?
        formulario = UsuarioForm(request.POST, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Usuario Modificado correctamente'
            return redirect(to= "usuarios")
        else:
            formulario = UsuarioForm()
            datos['mensaje'] = 'ERROR: No se ha modificado, intente nuevamente'
    return render(request,'xartgord/form_mod_usuario.html',datos)      

#ELIMINAR USUARIO
def form_mod_eliminar_usuario(request, id):
    usuario = Usuario.objects.get(Rut = id)
    usuario.delete()
    return redirect(to="usuarios")


