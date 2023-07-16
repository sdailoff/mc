from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'observacion']

        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'observacion': 'Observacion'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Observacion'}),     
        }