from django.db import models

# Create your models here.

class dashboard(models.Model):
    dashboard = models.CharField(max_length=40)
    camada = models.IntegerField()

class proveedores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

class analista(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)

#class Entregable(models.Model):
#    nombre = models.CharField(max_length=30)   

#    fecha_de_entrega = models.DateField()
#    entregado = models.BooleanField()       
