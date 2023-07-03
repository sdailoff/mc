from django.shortcuts import render

# Create your views here.
def homeMain(request):
    # Lógica de la vista
    
    return render(request, 'indexMain.html')