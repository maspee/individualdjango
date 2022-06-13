from django.shortcuts import render
from . models import Cliente

# Create your views here.

def index(request):
    return render(request,'monitoreo/index.html')

def contacto(request):
    return render(request,'monitoreo/contacto.html')

def recibir(request):
    return render(request, 'monitoreo/index.html')

def clientes(request):
    cliente= Cliente.objects.all()
    return render(request, 'monitoreo/clientes.html', {"data": cliente})

def ej(request):
    return render(request, 'monitoreo/ej.html')