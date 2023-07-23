from django import forms
from .models import ScheduleAG 

class ScheduleAGForm(forms.ModelForm):
     
    class Meta:
        model = ScheduleAG
        fields = ['date', 'hourIni', 'usuario']