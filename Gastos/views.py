from django.shortcuts import render,redirect
from .models import Gasto,Categoria,Proveedor
from .forms import GastoForm

#Create your views here.

def gastos(request):

    gastos =  Gasto.objects.all()
    categorias = Categoria.objects.all()
    proveedor = Proveedor.objects.all()
    
    form = GastoForm(initial ={"concepto":"luis"})
   
    print(form)
    
    

    if request.method == "POST" :

        formulario_contacto = GastoForm(data=request.POST)
        

        if formulario_contacto.is_valid():

            nombre = request.POST.get("concepto")
            costo = request.POST.get("costo")
            categoria = request.POST.get("categoria")
            proveedor = request.POST.get("proveedor")
            formulario_contacto.save()

            return redirect("/gastos/?valido")
        
        else:

            return redirect("/gastos/?fallido")


    return render(request, "gastos/gastos.html",{"gastos":gastos,"categorias":categorias, "proveedores":proveedor, "form": form})


    