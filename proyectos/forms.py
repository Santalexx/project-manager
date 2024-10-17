from django import forms
from .models import Proyecto, Tarea
from django.forms.widgets import DateInput
from django.core.exceptions import ValidationError
from datetime import datetime

class ProyectoForm(forms.ModelForm):
    fecha_inicio = forms.DateField(input_formats=['%d/%m/%Y', '%Y-%m-%d'])
    fecha_fin = forms.DateField(input_formats=['%d/%m/%Y', '%Y-%m-%d'])

    class Meta:
        model = Proyecto
        fields = ['nombre', 'descripcion', 'fecha_inicio', 'fecha_fin']

    def clean_fecha_inicio(self):
        fecha = self.cleaned_data['fecha_inicio']
        if isinstance(fecha, str):
            try:
                return datetime.strptime(fecha, '%d/%m/%Y').date()
            except ValueError:
                raise ValidationError('Ingrese una fecha válida en formato DD/MM/YYYY')
        return fecha

    def clean_fecha_fin(self):
        fecha = self.cleaned_data['fecha_fin']
        if isinstance(fecha, str):
            try:
                return datetime.strptime(fecha, '%d/%m/%Y').date()
            except ValueError:
                raise ValidationError('Ingrese una fecha válida en formato DD/MM/YYYY')
        return fecha    

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion', 'estado', 'asignado_a']