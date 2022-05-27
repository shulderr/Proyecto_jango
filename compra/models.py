from django.db import models

# Create your models here.

class pedidos(models.Model):
    nombre = models.CharField(max_length=255)
    documento = models.IntegerField(default=0)
    correo = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    departamento = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    telefono = models.IntegerField(default=0)

