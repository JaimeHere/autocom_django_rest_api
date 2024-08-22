from django.db import models
from autor import models as autor_models
# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True, blank=False)
    autor = models.ForeignKey(autor_models.Autor, related_name='libro', on_delete=models.PROTECT)
