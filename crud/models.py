from django.db import models
from django.utils import timezone


class Usuario(models.Model):
    apellido = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    dni = models.IntegerField(default=None)
    domicilio = models.CharField(max_length=200)
    nacimiento = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.apellido+" "+self.nombre