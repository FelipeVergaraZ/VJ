from django import forms
from django.forms import ModelForm
from .models import Mercancia

class MercanciaForm(ModelForm):
    class Meta:
        model = Mercancia
        fields = ['idproducto','nombreproducto','stockproducto','precioproducto','imagen',]
        

        