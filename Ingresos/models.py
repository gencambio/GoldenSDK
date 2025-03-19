from django.db import models

#Create your models here.

class Tratamiento(models.Model):
    nombre = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'tratamiento'
        verbose_name_plural = 'tratamientos'
    def __str__(self):
        return self.nombre
        

class Cliente(models.Model):

    nombre =    models.CharField(max_length= 50)
    created =   models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'

    def __str__(self):
        return self.nombre
    
    # Create your models here.
    #def __str__(self):
    #   return self.nombre


class Ingreso(models.Model):

    concepto =    models.CharField(max_length= 250)
    valor = models.FloatField()
    tratamiento = models.ForeignKey(Tratamiento, on_delete=models.CASCADE)
    cliente =  models.CharField(max_length=200)
    created =   models.DateTimeField(auto_now_add=True)
    abono =  models.FloatField()
    

