from django.contrib import admin

from .models import Categoria, Gasto, Proveedor

# Register your models here.

admin.site  .register([Categoria, Gasto, Proveedor] )



