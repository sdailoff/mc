from django.shortcuts import render

# Create your views here.
def listTasks(request):
    # Lógica de la vista
    
    return render(request, 'listTasks.html')


# Create your views here.
def nuevaTask(request):
    # Lógica de la vista
    
    return render(request, 'nuevaTask.html')