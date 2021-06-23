from django.shortcuts import render, redirect
from .models import Mercancia
from django import forms
from .forms import MercanciaForm

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

def form_mercancia(request):

    mercancia = Mercancia.objects.all()
    datos = {
        'mercancia':mercancia,
        'form':MercanciaForm()
    }


    if (request.method == 'POST'):
        formulario=MercanciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Datos Guardados correctamente'
    
    return render(request, 'xartgord/form_mercancia.html',datos)   


def form_mod_mercancia(request, id):
    mercancia = Mercancia.objects.get(idproducto=id)
    datos = {
        'form':MercanciaForm(instance=mercancia)
    }

    if (request.method == 'POST'):

        formulario=MercanciaForm(data=request.POST, instance=mercancia)

        if formulario.is_valid():
            formulario.save()
            datos['mensaje']= 'Datos modificados correctamente'

















