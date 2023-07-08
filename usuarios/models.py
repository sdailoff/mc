from django.db import models

# Create your models here.
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre