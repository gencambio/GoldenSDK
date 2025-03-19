from django.contrib import admin
from .models import Ingreso,Cliente,Tratamiento

# Register your models here.


admin.site.register([Ingreso, Cliente, Tratamiento])
