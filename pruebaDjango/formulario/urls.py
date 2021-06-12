from django.urls import path
from .views import armaduras, armas, home
from .views import personajes, contact, items
from .views import enemigos, mercancia, objetos

urlpatterns = [
    path('',home,name='home'),
    path('personajes/',personajes,name='personajes'),
    path('enemigos/',enemigos,name='enemigos'),
    path('contact/',contact,name='contact'),
    path('armaduras/',armaduras,name='armaduras'),
    path('objetos/',objetos,name='objetos'),
    path('armas/',armas,name='armas'),
    path('mercancia/',mercancia,name='mercancia'),
    path('items/',items,name='items')
    
    
]



