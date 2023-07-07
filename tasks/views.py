from django.shortcuts import render

# Create your views here.
def homeTasks(request):
    # Lógica de la vista
    
    return render(request, 'indexTasks.html')