from django.urls import path

from .views import lista_mercancia



urlpatterns = [

    path('lista_mercancia',lista_mercancia,name='lista_mercancia'),

]


