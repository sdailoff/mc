from django.shortcuts import render

# Create your views here.
def listCompras(request):
    # Lógica de la vista
    
    return render(request, 'listCompras.html')


# Create your views here.
def nuevaCompra(request):
    # Lógica de la vista
    
    return render(request, 'indexCompras.html')