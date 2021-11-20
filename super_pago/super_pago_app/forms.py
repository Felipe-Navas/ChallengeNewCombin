from datetime import date
from django.forms import ModelForm
from django import forms

from .models import Boleta, Transaccion

class FormBoleta(ModelForm):
    class Meta:
        model = Boleta
        fields = [
            'codigo_barra',
            'tipo',
            'descripcion',
            'fecha_vto',
            'importe',
        ]
        widgets = {
            'codigo_barra': forms.TextInput(attrs={'class':'form-control  mb-3', 'placeholder':'Ingresar el codigo de barras', 'type':'text'}),
            'tipo': forms.Select(attrs={'class':'form-control mb-3'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Ingresar la descripcion', 'type':'text'}),
            'fecha_vto': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control  mb-3', 'placeholder':'Seleccione una fecha', 'type':'date'}),
            'importe': forms.NumberInput(attrs={'class':'form-control mb-3'}),
        }

class FormTransaccion(ModelForm):
    class Meta:
        model = Transaccion
        fields = [
            'codigo_barra',
            'metodo',
            'numero_tarjeta',
            'importe',
        ]
        widgets = {
            'codigo_barra': forms.TextInput(attrs={'class':'form-control  mb-3', 'placeholder':'Ingresar el codigo de barras', 'type':'text'}),
            'metodo': forms.Select(attrs={'class':'form-control mb-3'}),
            'numero_tarjeta': forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Ingresar el numero de la tarjeta', 'type':'text', 'required': False}),
            'importe': forms.NumberInput(attrs={'class':'form-control mb-3'}),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        metodo = cleaned_data.get("metodo")
        numero_tarjeta = cleaned_data.get("numero_tarjeta")

        if metodo != 'Efectivo':
            if not numero_tarjeta or numero_tarjeta == '':
                self.add_error("numero_tarjeta",
                               "Ingresar el numero de la tarjeta!")

class FiltoFechaForm(forms.Form):
    fecha_desde = forms.DateField(initial=date.today)
    fecha_hasta = forms.DateField(initial=date.today)
