from django.shortcuts import render,redirect
from .models import Ingreso,Cliente,Tratamiento
from .forms import IngresoForm

#Create your views here.

def ingresos(request):
   
   

    ingresos =  Ingreso.objects.all()
    tratamientos = Tratamiento.objects.all()
    clientes = Cliente.objects.all()
    
    form = IngresoForm()

    if request.method == "POST" :

        formulario_contacto = IngresoForm(data=request.POST)
        

        if formulario_contacto.is_valid():

            nombre = request.POST.get("concepto")
            valor = request.POST.get("valor")
            categoria = request.POST.get("tratamiento")
            proveedor = request.POST.get("cliente")
            abono = request.POST.get("abono")
            formulario_contacto.save()

            return redirect("/ingresos/?valido")
        
        else:

            return redirect("/ingresos/?fallido")


    return render(request, "ingresos/ingresos.html",{"ingresos":ingresos,"tratamientos":tratamientos, "clientes":clientes, "form": form})

   