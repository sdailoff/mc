from django.shortcuts import render, redirect, get_object_or_404

from .models import Usuario, Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from usuarios.models import Usuario
# Create your views here.
def listTasks(request):
    # Lógica de la vista
    listado = Task.objects.all()
    return render(request, 'listTasks.html',  {'tareas': listado})


# Create your views here.
def nuevaTask(request):
    # Lógica de la vista
    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            pk = request.POST.get('id')

            if pk:  # Si se proporciona una clave primaria, es una actualización
                objeto = get_object_or_404(Usuario, id=pk)
                objeto.contraseña = form.data.contraseña
                objeto.save()
                  # Actualiza los datos en la base de datos
            else:
                form.save() # Guarda los datos en la base de datos
            return redirect('listTasks')  # Redirecciona a una página de éxito o a donde desees
        else:
            form.nombre.errors='No pudo guardar'

    else:
        listado = Usuario.objects.all()
        print(listado)
        return render(request, 'nuevaTask.html', {'empleados': listado})
    
    listado = Usuario.objects.all()
    print(listado)
    return render(request, 'nuevaTask.html', {'empleados': listado})

    
def editarTask(request, id):
    ta = get_object_or_404(Task, id=id)

    if request.method == 'GET':                 
        form = TaskForm(instance=ta)
        return render(request, 'nuevaTask.html', {'form': form, 'tarea': ta})
    else:
        form = TaskForm(request.POST, instance=ta)
        if form.is_valid():
            form.save()  # Guarda los datos actualizados en el objeto 'usu'
            return redirect('listTasks')
        else:
            return render(request, 'nuevaTask.html', {'form': form, 'tarea': ta})
    
@login_required
def eliminarTask(request, id):
    
    usu = get_object_or_404(Task, id=id)
    usu.delete()
    return redirect('listTasks')
         


    