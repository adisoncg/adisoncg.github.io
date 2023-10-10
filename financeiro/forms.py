# financeiro/forms.py
from django import forms
from .models import Receita, Despesa
from django.forms.widgets import DateInput, NumberInput

# Lista de opções de categoria
CATEGORIA_CHOICES = [

    ('alimentacao', 'Alimentação'),
    ('moradia', 'Moradia'),
    ('estudo', 'Estudo'),
    ('saude', 'Saúde'),
    ('transporte', 'Transporte'),
    ('vestuario', 'Vestuário'),
    ('lazer', 'Lazer'),
    ('outro', 'Outro'),
    
]

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['descricao', 'valor', 'data']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
            'valor': NumberInput(attrs={'value': '0.00'}),
        }
class DespesaForm(forms.ModelForm):

    categoria = forms.ChoiceField(choices=CATEGORIA_CHOICES, label='Categoria')
    class Meta:
        model = Despesa
        fields = ['descricao', 'valor', 'data', 'categoria']
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
            'valor': NumberInput(attrs={'value': '0.00'}),
        }
