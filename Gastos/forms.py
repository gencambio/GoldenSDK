from django import forms
from .models import Gasto,Categoria,Proveedor

class GastoForm(forms.ModelForm):

    class Meta:
        model = Gasto
        fields=['concepto', 'costo', 'categoria', 'proveedor'] 

