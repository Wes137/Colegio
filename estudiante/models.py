from django.db import models

# Create your models here.
class estudiante(models.Model):
  nombre_estudiante = models.CharField(max_length=200)

  def __str__(self):
    return self.nombre_estudiante