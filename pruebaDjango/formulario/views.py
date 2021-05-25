from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'formulario/index.html')

def personajes(request):
    return render(request, 'formulario/personajes.html')

def items(request):
    return render(request, 'formulario/items.html')






