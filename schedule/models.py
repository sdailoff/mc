from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    dia = models.DateField()
    hora = models.TimeField()
    usuario1 = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules_usuario1', default = 99)
    usuario2 = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules_usuario2', default = 99)
    usuario3 = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules_usuario3', default = 99)
    usuario4 = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='schedules_usuario4', default = 99)

    def __str__(self):
        return f"Calendario para el día {self.dia} a las {self.hora}"
    