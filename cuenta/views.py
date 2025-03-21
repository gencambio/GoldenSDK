from django.shortcuts import render,redirect
from Gastos.models import Gasto,Categoria,Proveedor
import datetime

from Gastos.forms import GastoForm

# Create your views here.


#def modificar_gasto(request, gasto_id):
    #gasto = Gasto(request)   # crea el gasto

    #gasto  = Gasto.objects.get(id = gasto_id)

    #carro.agregar(producto)

    #return redirect('Tienda')
'''def agregar_cuenta(request, producto_id):
    cuenta = Cuenta(request)   # crea el carro 

    gasto  = Producto.objects.get(id = producto_id)

    cuenta.agregar(gasto)

    return redirect('Tienda')'''

def eliminar_gasto(request, gasto_id):
   # carro = Carro(request)   # crea el carro 

    gasto  = Gasto.objects.get(id = gasto_id)
    gasto.delete()
  

    return redirect('Gastos')

def fecha_gasto(request):
   # carro = Carro(request)   # crea el carro 
    if request.method == "POST" :
        fecha_inicial = request.POST.get("fecha_inicial")
        fecha_final = request.POST.get("fecha_final")
        categoria = request.POST.get("categoria")
    #print(fecha_inicial,'fecha')
    #return redirect('Gastos',{'gastos':gasto})
    gastos =  Gasto.objects.filter(created__gt = fecha_inicial, created__lt= fecha_final, categoria__eq= categoria)
    #print(cuenta) #print(gastos1, "gastos1")
    #gastos = Gasto.objects.all()
    #print(gastos)
    categorias = Categoria.objects.all()
    proveedor = Proveedor.objects.all()
    
    form = GastoForm(initial ={"concepto":"luis"})

    return render(request, "gastos/gastos.html",{"gastos":gastos,"categorias":categorias, "proveedores":proveedor, "form": form})


