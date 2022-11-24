from django.db import models

# Create your models here.
class Sucursales(models.Model):

    direccion=models.CharField(max_length=40)
    telefono= models.IntegerField()

class Productos(models.Model):

    descripcion_del_producto=models.CharField(max_length=40)
    marca=models.CharField(max_length=50)
    precio= models.IntegerField()

class Ofertas(models.Model):

    descripcion_del_producto=models.CharField(max_length=100)
    marca=models.CharField(max_length=50)
    precio= models.IntegerField()
    descuento=models.CharField(max_length=50)