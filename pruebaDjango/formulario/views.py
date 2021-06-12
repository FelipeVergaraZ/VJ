from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'xartgord/index.html')

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
