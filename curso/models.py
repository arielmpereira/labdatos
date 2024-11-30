from django.db import models

# Create your models here.
class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

