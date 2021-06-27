from django.db import models

# Create your models here.


class Rango(models.Model):
    idRango = models.IntegerField(primary_key=True,verbose_name='Id de Rango')
    nombreRango= models.CharField(max_length=50,verbose_name='Nombre deL Rango')

def __str__(self):
    return self.nombreRango


class Usuario(models.Model):
    idUsuario=models.IntegerField(primary_key=True,verbose_name='Id de Usuario')
    nombreusuario=models.CharField(max_length=20,verbose_name='Nombre del usuario')
    contraseñausuario=models.CharField(max_length=20,verbose_name='Contraseña del usuario')
    rango=models.ForeignKey(Rango, on_delete=models.CASCADE)

def __str__(self):
    return self.nombreusuario

class Mercancia(models.Model):
    idproducto=models.IntegerField(primary_key=True,verbose_name='Id del Producto')
    nombreproducto=models.CharField(max_length=20,verbose_name='Nombre del Producto')
    stockproducto=models.IntegerField(verbose_name='Stock del producto')
    precioproducto=models.IntegerField(verbose_name='Precio del producto')
    imagen=models.ImageField(upload_to='Imagenes',null=True) 
def __str__(self):
    return self.nombreproducto



