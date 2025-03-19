from django import forms
from .models import Ingreso,Cliente,Tratamiento

class IngresoForm(forms.ModelForm):

    class Meta:
        model = Ingreso
        fields=['concepto', 'valor', 'tratamiento', 'cliente','abono'] 

