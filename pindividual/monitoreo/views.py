from django.shortcuts import redirect, render
from . models import Cliente
from .forms import ReclamoForm, ClienteForm

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

def reclamo(request):
    datos=  request.POST
    email= datos["email"]
    reclamo= datos["reclamo"]
    print(datos, email,reclamo)
    return render(request, 'monitoreo/contacto.html', {'mensaje': "Datos Recibidos", "email": email})

def reclamo2(request):
    if request.method == "POST":
        form= ReclamoForm(data= request.POST)
        email= form["email"]
        reclamo= ["reclamo"]
        return render(request, "monitoreo/reclamoejemplo.html", {"respuesta": "OK"})
    else:
        form= ReclamoForm()
        return render(request, 'monitoreo/reclamoejemplo.html', {"form": form})

def clientes2(request):
    if request.method=="POST":
        form= ClienteForm(data= request.POST)
        if form.is_valid():
            form.save()
            #cliente= form.save(commit=False) #esta en memoria
            #cliente.save() #guarda en bd
        return redirect('/clientes')
    else:
        form= ClienteForm()
        return render(request, 'monitoreo/crearcliente.html', {"form": form})

def ej(request):
    return render(request, 'monitoreo/ej.html')

#Vistas
