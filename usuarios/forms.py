from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'usuario', 'contraseña']

        labels = {
            'nombre': 'Nombre',
            'usuario': 'Usuario',
            'contraseña': 'Contraseña'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'usuario': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'contraseña': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),     
        }