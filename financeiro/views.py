# financeiro/views.py
from django.shortcuts import render, redirect
from .models import Receita, Despesa
from .forms import ReceitaForm, DespesaForm
from django.contrib.auth.decorators import login_required


@login_required
def adicionar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            nova_receita = form.save(commit=False)
            nova_receita.usuario = request.user
            nova_receita.save()
            return redirect('adicionar_receita')
    else:
        form = ReceitaForm()
    
    receitas = Receita.objects.filter(usuario=request.user)
    return render(request, 'registration/adicionar_receita.html', {'form': form, 'receitas': receitas})

def delete_receita(request, receita_id):
    receita = Receita.objects.get(pk=receita_id)
    receita.delete()
    return redirect('adicionar_receita')

@login_required
def adicionar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            nova_despesa = form.save(commit=False)
            nova_despesa.usuario = request.user
            nova_despesa.save()
            return redirect('adicionar_despesa')
    else:
        form = DespesaForm()
    
    despesas = Despesa.objects.filter(usuario=request.user)
    return render(request, 'registration/adicionar_despesa.html', {'form': form, 'despesas': despesas})

def delete_despesa(request, despesa_id):
    despesa = Despesa.objects.get(pk=despesa_id)
    despesa.delete()
    return redirect('adicionar_despesa')

