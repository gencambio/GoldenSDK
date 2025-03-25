from django.urls import path
from . import views

app_name= "gastos_edit"

urlpatterns = [
    
    
    path('eliminar/<int:gasto_id>/', views.eliminar_gasto, name = "eliminar"),
    path('fecha/', views.fecha_gasto, name = "fecha_gasto"),
    path('eliminar_ingreso/<int:ingreso_id>/', views.eliminar_ingreso, name = "eliminar_ingreso"),

   # path('restar/<int:producto_id>/', views.restar_producto, name = "restar"),

  
]
