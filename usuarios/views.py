from django.shortcuts import render
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
def indexUser(request):
    # Lógica de la vista    
    return render(request, 'indexUser.html')


def indexEmpleados(request):
    # Lógica de la vista    
    return render(request, 'indexEmpleados.html')


def newEmpleado(request):
    # Lógica de la vista   
    form =  UsuarioForm()
    return render(request, 'user.html', {'form': form})
