from django.shortcuts import render, redirect, get_object_or_404
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
            pk = request.POST.get('id')

            if pk:  # Si se proporciona una clave primaria, es una actualización
                objeto = get_object_or_404(Usuario, id=pk)
                objeto.contraseña = form.data.contraseña
                objeto.save()
                  # Actualiza los datos en la base de datos
            else:
                form.save() # Guarda los datos en la base de datos
            return redirect('listEmpleados')  # Redirecciona a una página de éxito o a donde desees
        else:
            form.nombre.errors='No pudo guardar'

    else:
        form =  UsuarioForm()

    return render(request, 'nuevoEmpleado.html', {'form': form})


def editarEmpleado(request, id):
    usu = get_object_or_404(Usuario, id=id)

    if request.method == 'GET':                 
        form = UsuarioForm(instance=usu)
        return render(request, 'nuevoEmpleado.html', {'form': form, 'usu': usu})
    else:
        form = UsuarioForm(request.POST, instance=usu)
        if form.is_valid():
            form.save()  # Guarda los datos actualizados en el objeto 'usu'
            return redirect('listEmpleados')
        else:
            return render(request, 'nuevoEmpleado.html', {'form': form, 'usu': usu})
    
    
   