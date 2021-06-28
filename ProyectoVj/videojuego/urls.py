from django.urls import path
from .views import form_reg_usuario, form_usuario, home, items, listas, polerones, registro, usuario
from .views import personajes, contact
from .views import enemigos, mercancia
from .views import armaduras, armas, home
from .views import personajes, contact, items
from .views import enemigos, mercancia, objetos,cuenta
from .views import form_mercancia, form_modifimerca,form_eliminar

urlpatterns = [
    path('',home,name='home'),
    path('personajes/',personajes,name='personajes'),
    path('enemigos/',enemigos,name='enemigos'),
    path('contact/',contact,name='contact'),
    path('armaduras/',armaduras,name='armaduras'),
    path('objetos/',objetos,name='objetos'),
    path('armas/',armas,name='armas'),
    path('mercancia/',mercancia,name='mercancia'),
    path('items/',items,name='items'),
    path('cuenta/',cuenta,name='cuenta'),
    path('polerones/',polerones,name='polerones'),
    path('registro/',registro,name='registro'),
    path('usuario/',usuario,name='usuario'),
    path('form_mod_usuario/',form_reg_usuario,name='form_mod_usuario'),
    path('form_usuario/',form_usuario,name='from_usuario'),
    path('form_mercancia/',form_mercancia,name='form_mercancia'),
    path('listas/',listas,name='listas'),
    path('form_modifimerca/<id>/',form_modifimerca,name='form_modifimerca'),
    path('form_eliminar/<id>/',form_eliminar,name='form_eliminar'),
]


