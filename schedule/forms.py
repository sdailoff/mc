from django import forms
from .models import Schedule

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['dia', 'hora', 'usuario1', 'usuario2', 'usuario3','usuario4']