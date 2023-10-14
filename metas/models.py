from django.db import models
from django.conf import settings

class Meta(models.Model):
    TIPO_PRAZO_CHOICES = [
        ('curto prazo', 'Curto Prazo'),
        ('medio prazo', 'Médio Prazo'),
        ('longo prazo', 'Longo Prazo'),
    ]

    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor_meta = models.DecimalField(max_digits=10, decimal_places=2)
    data_vencimento = models.DateField()
    tipo_prazo = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
