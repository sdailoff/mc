from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=10)    
    
class HourIni(models.Model):
    id = models.AutoField(primary_key=True)
    hourIni = models.TimeField() 
 

class ScheduleAG(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    hourIni = models.ForeignKey(HourIni, on_delete=models.CASCADE) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=99)

