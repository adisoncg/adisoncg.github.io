# financeiro/models.py
from django.db import models
from django.conf import settings

class Receita(models.Model):
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
    
    class Meta:
        app_label = 'financeiro'

class Despesa(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    categoria = models.CharField(max_length=100) 
    categoria = models.CharField(max_length=20, choices=[
        ('alimentacao', 'Alimentação'),
        ('moradia', 'Moradia'),
        ('estudo', 'Estudo'),
        ('saude', 'Saúde'),
        ('transporte', 'Transporte'),
        ('vestuario', 'Vestuário'),
        ('lazer', 'Lazer'),
        ('outro', 'Outro'),
])


    def __str__(self):
        return self.descricao
    
    class Meta:
        app_label = 'financeiro'
