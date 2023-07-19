from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    inicio = models.ManyToManyField('HourIni') 
    usuario1 = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules_usuario1', default = 99)

    def __str__(self):
        return f"Calendario para el día {self.dia} a las {self.hora}"
    
class HourIni(models.Model):
    id = models.AutoField(primary_key=True)
    hourIni = models.TimeField()