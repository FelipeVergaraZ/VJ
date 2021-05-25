from django.urls import path
from .views import home, items
from .views import personajes

urlpatterns = [
    path('',home,name='home'),
    path('personajes/',personajes,name='personajes'),
    path('items/',items,name='items')
    
]



