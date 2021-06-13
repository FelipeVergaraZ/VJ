from django.shortcuts import render
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
    context= {"nombre":"AAAAAAAAAAAAA","usuario":"admin"}
    return render(request, 'xartgord/contact.html', context)

def mercancia(request):
    return render(request, 'xartgord/mercancia.html')

def form_mercancia(request):
    datos = {
        'form':MercanciaForm()
    }

    if (request.method == 'POST'):
        formulario=MercanciaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Guardados correctamente'
    return render(request, 'xartgord/form_mercancia.html',datos)

