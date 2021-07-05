
from django.urls import path

from rest_producto.views import lista_mercancia,detalle_categoria
from rest_producto.viewsLogin import login



urlpatterns = [

    path('lista_mercancia',lista_mercancia,name='lista_mercancia'),
    path('detalle_categoria',detalle_categoria,name='detalle_categoria'),
]


