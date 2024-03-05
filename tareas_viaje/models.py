from django.db import models
from django.contrib.auth.models import User

class TareaViaje(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    completada = models.BooleanField(default=False)

    def __str__(self):
        return f"Tarea de {self.usuario.username}: {self.destino}"

