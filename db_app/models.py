from django.db import models

# Create your models here.

class Persona(models.Model):
    referencia = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    nuevo = models.BooleanField()
    descripcion = models.TextField()
