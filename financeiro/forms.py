# financeiro/forms.py
from django import forms
from .models import Receita, Despesa
from django.forms.widgets import DateInput, NumberInput

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
            'valor': NumberInput(attrs={'value': '0.00'}),
        }
class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
            'valor': NumberInput(attrs={'value': '0.00'}),
        }
