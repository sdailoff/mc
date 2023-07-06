from django.shortcuts import render

# Create your views here.
def indexUser(request):
    # Lógica de la vista
    
    return render(request, 'indexUser.html')