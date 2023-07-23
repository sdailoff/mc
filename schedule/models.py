from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Date(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=10)    
    
class HourIni(models.Model):
    id = models.AutoField(primary_key=True)
    hourIni = models.TimeField() 
 

class ScheduleAG(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE)
    hourIni = models.ManyToManyField(HourIni) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=99)

