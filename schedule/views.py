from django.shortcuts import render, redirect, get_object_or_404

from .models import Date, Usuario, ScheduleAG, HourIni
from .forms import ScheduleAGForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from itertools import groupby

from usuarios.models import Usuario
# Create your views here.
def listSchedules(request):
    # Lógica de la vista
    listado = ScheduleAG.objects.all().order_by("date", "hourIni")
        

    data = ScheduleAG.objects.all()

    x = [list(result) for key, result  in groupby(data, key=lambda item: item.date)]    
    #print(x)
    for xyz in x:
        print (xyz[0])
#    grouped = dict()
#    for obj in ScheduleAG.objects.all():
#        grouped.setdefault(obj.date, []).append(obj)
        #print(obj.usuario)


#    print (grouped)

#    for sc in grouped:        
#        print (grouped[sc])

#    for x,y in grouped.items():
#        print(x,y)

    return render(request, 'listSchedules.html',  {'schedules': listado})


# Create your views here.
def nuevoSchedule(request):
    # Lógica de la vista
    if request.method == 'POST':
        form = ScheduleAGForm(request.POST)
         
        if form.is_valid():
            
            
            pk = request.POST.get('id')

            if pk:  # Si se proporciona una clave primaria, es una actualización
                objeto = get_object_or_404(ScheduleAG, id=pk)
                objeto.date = form.data.date
                
                objeto.save()
                  # Actualiza los datos en la base de datos
            else:
                form.save() # Guarda los datos en la base de datos
            return redirect('listSchedules')  # Redirecciona a una página de éxito o a donde desees
        else:
            print(form.data)
            print(form.errors)
            #form.errors='No pudo guardar'

    else:
        listado = Usuario.objects.all()
        listHoras = HourIni.objects.all().order_by('hourIni')
        listDate = Date.objects.all()
        return render(request, 'nuevoSchedule.html', {'empleados': listado, 'listHoras': listHoras, 'listDate': listDate})
    
    listado = Usuario.objects.all()
    listHoras = HourIni.objects.all().order_by('hourIni')
    listDate = Date.objects.all()
    return render(request, 'nuevoSchedule.html', {'empleados': listado, 'listHoras': listHoras, 'listDate': listDate})

def editarSchedule(request, id):
    sche = get_object_or_404(ScheduleAG, id=id)
    listado = Usuario.objects.all()

    if request.method == 'POST':
        form = ScheduleAGForm(request.POST, instance=sche)
        if form.is_valid():
            form.save()
            return redirect('listSchedules')
    else:
        form = ScheduleAGForm(instance=sche)
    
    return render(request, 'nuevoSchedule.html', {'form': form, 'Schedule': sche, 'empleados': listado})

    
@login_required
def eliminarSchedule(request, id):
    
    sche = get_object_or_404(ScheduleAG, id=id)
    sche.delete()
    return redirect('listSchedules')