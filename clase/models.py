from django.db import models
from estudiante.models import estudiante

# Create your models here.
class clase(models.Model):
  nombre = models.CharField(max_length=200)
  estudiantes = models.ForeignKey(estudiante, on_delete=models.CASCADE)

  def __str__(self):
    return self.nombre