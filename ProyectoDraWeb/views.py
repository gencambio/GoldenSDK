from django.shortcuts import render
from cuenta.cuenta import Cuenta

# Create your views here.

def home(request):


    cuenta = Cuenta(request)
    
    return render(request, "ProyectoDraWeb/home.html")