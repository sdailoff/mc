from django.shortcuts import render, redirect, get_object_or_404
from .forms import UsuarioForm
from .models import Usuario

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 

# Create your views here.
def loginSession(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            
            usu = form.cleaned_data['usuario'] 
            passw  = form.cleaned_data['contraseña'] 
            user = authenticate(request, username=usu, password=passw)
            if user is not None:

                user = User.objects.get(username=usu)

                # Iniciar sesión del usuario
                login(request, user)
                
                listado = Usuario.objects.all()
                return render(request, 'listEmpleados.html',  {'empleados': listado})
                # Redirigir a una página después de iniciar sesión correctamente
                #return render(request, 'login/login.html', {'mensaje': 'Inicio de sesión correccctooooo'})
            else:
                return render(request, 'login.html', {'mensaje': 'Inicio de sesión erroneo'})
            # Realizar lógica de autenticación
            # ...    
        else:
            
            return render(request, 'login.html', {'mensaje': form.errors})

    else:
        return render(request, 'login.html')# Lógica de la vista    
    #return render(request, 'login.html')
    return render(request, 'login.html')


def logoutSession(request):
    logout(request)
    return render(request, 'login.html')# Lógica de la vista    

def listEmpleados(request):
    # Lógica de la vista    
    listado = Usuario.objects.all()
    return render(request, 'listEmpleados.html',  {'empleados': listado})

@login_required
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
    

def eliminarEmpleado(request, id):
    
    usu = get_object_or_404(Usuario, id=id)
    usu.delete()
    return redirect('listEmpleados')
         


def logoutSession(request):
    logout(request)
    return render(request, 'login.html')