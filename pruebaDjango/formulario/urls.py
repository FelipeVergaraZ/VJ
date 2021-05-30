from django.urls import path
from .views import home, items
from .views import personajes, contact
from .views import enemigos, mercancia

urlpatterns = [
    path('',home,name='home'),
    path('personajes/',personajes,name='personajes'),
    path('enemigos/',enemigos,name='enemigos'),
    path('contact/',contact,name='contact'),
    path('mercancia/',mercancia,name='mercancia'),
    path('items/',items,name='items')
    
]



