from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'wikigame/index.html')

def items(request):

    return render(request, 'wikigame/items.html')

