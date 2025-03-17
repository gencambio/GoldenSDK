from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self):
        return self.nombre
        

class Proveedor(models.Model):

    nombre =    models.CharField(max_length= 50)
    created =   models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    def __str__(self):
        return self.nombre
    
    # Create your models here.
    #def __str__(self):
    #   return self.nombre


class Gasto(models.Model):

    concepto =    models.CharField(max_length= 50)
    costo = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor =  models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    created =   models.DateTimeField(auto_now_add=True)
    




