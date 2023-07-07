from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario

# Create your views here.
def login(request):
    # Lógica de la vista    
    return render(request, 'login.html')


def listEmpleados(request):
    # Lógica de la vista    
    listado = Usuario.objects.all()
    return render(request, 'listEmpleados.html',  {'empleados': listado})

def nuevoEmpleado(request):
    # Lógica de la vista   
    

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda los datos en la base de datos
            
            return redirect('listEmpleados')  # Redirecciona a una página de éxito o a donde desees
        else:
            form.nombre.errors='No puede tener más de 100 caracteres'

    else:
        form =  UsuarioForm()

    return render(request, 'nuevoEmpleado.html', {'form': form})

