from django.shortcuts import render,redirect
from django.views.generic import View
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.



class VRegistro(View):

    def get(self, request):
        
        form = UserCreationForm()
        return render(request, 'registro/registro.html',{"form": form})
    
    def post(self, request):
        
        form = UserCreationForm(request.POST)
        
        if form.is_valid():

            usuario = form.save()

            login(request, usuario)

            return redirect("HomeA")

        else:
            for msg in form.error_messages:

                messages.error(request, form.error_messages[msg])

            return render(request, 'registro/registro.html',{"form": form})
        
def cerrar_sesion(request):
    
    logout(request)
    
    return redirect("HomeA")


def logear(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            
            nombre = form.cleaned_data.get("username")
            
            contrase = form.cleaned_data.get("password")

            usuario = authenticate(username=nombre, password = contrase)

            if usuario is not None:
                login(request ,usuario)

                return redirect("HomeA")
            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "formulario no valido")
    else:
        form = AuthenticationForm()

    return render(request, 'login/login.html',{"form": form})