from django.urls import path

from .views import lista_categoria



urlpatterns = [

    path('lista_categoria',lista_categoria,name='lista_categoria'),

]


