from django.db import models


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

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de Categoria')
    nombreCategoria= models.CharField(max_length=50,verbose_name='Nombre deL Categoria')

def __str__(self):
    return self.nombreCategoria


class Mercancia(models.Model):
    idproducto=models.IntegerField(primary_key=True,verbose_name='Id del Producto')
    nombreproducto=models.CharField(max_length=20,verbose_name='Nombre del Producto')
    stockproducto=models.IntegerField(verbose_name='Stock del producto')
    precioproducto=models.IntegerField(verbose_name='Precio del producto')
    imagen=models.ImageField(upload_to='Imagenes',null=True)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

def __str__(self):
    return self.nombreproducto

    
