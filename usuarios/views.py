from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from financeiro.models import Despesa, Receita

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('dashboard') 
        else:
            messages.error(request, 'Erro de autenticação. Verifique suas credenciais.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')  

#dashboard exibição 
@login_required
def calcular_total_despesas(request):
    total_despesas = Despesa.objects.filter(usuario=request.user).aggregate(Sum('valor'))['valor__sum']
    return total_despesas or 0

@login_required
def calcular_total_receitas(request):
    total_receitas = Receita.objects.filter(usuario=request.user).aggregate(Sum('valor'))['valor__sum']
    return total_receitas or 0

@login_required
def calcular_saldo(request):
    total_despesas = Despesa.objects.filter(usuario=request.user).aggregate(Sum('valor'))['valor__sum'] or 0
    total_receitas = Receita.objects.filter(usuario=request.user).aggregate(Sum('valor'))['valor__sum'] or 0
    saldo = total_receitas - total_despesas
    return saldo

from django.shortcuts import render
from financeiro.models import Despesa
from django.contrib.auth.decorators import login_required
from django.db import models  # Certifique-se de importar models do Django

@login_required
def dashboard(request):
    # Código para calcular o total de despesas e receitas
    total_despesas = calcular_total_despesas(request)
    total_receitas = calcular_total_receitas(request)
    saldo = total_receitas - total_despesas

    # Código para calcular o total de gastos e porcentagens de gastos por categoria
    despesas = Despesa.objects.filter(usuario=request.user)
    total_gastos = despesas.aggregate(total=models.Sum('valor'))['total'] or 0
    categorias = ['alimentacao', 'moradia', 'estudo', 'saude', 'transporte', 'vestuario', 'lazer', 'outro']
    porcentagens = {}
    for categoria in categorias:
        gastos_categoria = despesas.filter(categoria=categoria).aggregate(total=models.Sum('valor'))['total'] or 0
        if total_gastos > 0:
            porcentagem = (gastos_categoria / total_gastos) * 100
        else:
            porcentagem = 0
        porcentagens[categoria] = porcentagem

    return render(request, 'registration/dashboard.html', {
        'total_despesas': total_despesas,
        'total_receitas': total_receitas,
        'saldo': saldo,
        'total_gastos': total_gastos,
        'porcentagens': porcentagens,
    })
