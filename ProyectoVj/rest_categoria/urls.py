from django.urls import path

from rest_categoria.views import lista_categoria
from rest_categoria.viewsLogin import login


urlpatterns = [

    path('lista_categoria',lista_categoria,name='lista_categoria'),
    path('login',login,name='login'),
]


