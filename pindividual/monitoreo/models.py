from tkinter.messagebox import NO
import django
from django.db import models
import django.utils.timezone

# Create your models here.

class Cliente(models.Model):
    rut=models.CharField(max_length=10, unique=True)
    nombre=models.CharField(max_length=50, default=None)
    apellido=models.CharField(max_length=100, default=None)
    edad = models.IntegerField(default=None)
    direccion=models.CharField(max_length=100, default=None)
    correo=models.CharField(max_length=50, default=None)
    telefono=models.IntegerField(default=None)
    receta=models.CharField(max_length=100, default=None)
    fecha_inicio=models.DateTimeField(default=django.utils.timezone.now)
    remedio=models.CharField(max_length=100, default=None)
    horario=models.TimeField(default=None)