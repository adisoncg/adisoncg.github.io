from django import forms
from .models import Meta
from django.forms.widgets import DateInput

TIPO_PRAZO_CHOICES = [
    ('curto prazo', 'Curto Prazo'),
    ('medio prazo', 'Médio Prazo'),
    ('longo prazo', 'Longo Prazo'),
]

class MetaForm(forms.ModelForm):
    nome = forms.CharField(max_length=100, required=True)
    descricao = forms.CharField(max_length=255)
    valor_meta = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    data_vencimento = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        label='Data de Vencimento'
    )
    tipo_prazo = forms.ChoiceField(
        choices=TIPO_PRAZO_CHOICES,
        label='Tipo de Prazo'
    )
    
    class Meta:
        model = Meta
        fields = ['nome', 'descricao', 'valor_meta', 'data_vencimento', 'tipo_prazo']


