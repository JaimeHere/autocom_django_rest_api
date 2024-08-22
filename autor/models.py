from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    fecha_nacimiento = models.DateField(auto_now_add=True)