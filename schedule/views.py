from django.shortcuts import render, redirect, get_object_or_404

from .models import Usuario, Schedule, HourIni
from .forms import ScheduleForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from usuarios.models import Usuario
# Create your views here.
def listSchedules(request):
    # Lógica de la vista
    listado = Schedule.objects.all()
    return render(request, 'listSchedules.html',  {'schedules': listado})


# Create your views here.
def nuevoSchedule(request):
    # Lógica de la vista
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        
        if form.is_valid():
            pk = request.POST.get('id')

            if pk:  # Si se proporciona una clave primaria, es una actualización
                objeto = get_object_or_404(Schedule, id=pk)
                objeto.date = form.data.date
                
                objeto.save()
                  # Actualiza los datos en la base de datos
            else:
                form.save() # Guarda los datos en la base de datos
            return redirect('listSchedules')  # Redirecciona a una página de éxito o a donde desees
        else:
            print(form.errors)
            form.errors='No pudo guardar'

    else:
        listado = Usuario.objects.all()
        listHoras = HourIni.objects.all()
        return render(request, 'nuevoSchedule.html', {'empleados': listado, 'listHoras': listHoras})
    
    listHoras = HourIni.objects.all().order_by('hourIni')
    listado = Usuario.objects.all()
     
    return render(request, 'nuevoSchedule.html', {'empleados': listado, 'listHoras': listHoras})

def editarSchedule(request, id):
    sche = get_object_or_404(Schedule, id=id)
    listado = Usuario.objects.all()

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=sche)
        if form.is_valid():
            form.save()
            return redirect('listSchedules')
    else:
        form = ScheduleForm(instance=sche)
    
    return render(request, 'nuevoSchedule.html', {'form': form, 'Schedule': sche, 'empleados': listado})

    
@login_required
def eliminarSchedule(request, id):
    
    sche = get_object_or_404(Schedule, id=id)
    sche.delete()
    return redirect('listSchedules')