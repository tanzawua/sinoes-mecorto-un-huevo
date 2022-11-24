
from unittest.util import _MAX_LENGTH
from django.db import models


class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models
    referencia = models.CharField(max_length=200)
    precio = models.IntegerField()
    nuevo = models.BooleanField()
    descripcion = models.TextField()
    image = models.ImageField(upload_to="media" )
    fecha = models.DateField(auto_now_add=True)

