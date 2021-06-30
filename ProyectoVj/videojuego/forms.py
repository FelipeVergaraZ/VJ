from django import forms
from django.forms import ModelForm
from .models import Mercancia,Usuario

class MercanciaForm(ModelForm):
    class Meta:
        model = Mercancia
        fields = ['idproducto','nombreproducto','stockproducto','precioproducto','categoria','imagen']
        

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['Rut', 'Contra', 'Nombre', 'Apellidos','Mail','Telefono', 'Direccion'] 