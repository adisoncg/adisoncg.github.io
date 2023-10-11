from django.shortcuts import render, redirect
from .models import Receita, Despesa
from .forms import ReceitaForm, DespesaForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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

    paginator = Paginator(receitas, 5) 
    page = request.GET.get('page')

    try:
        receitas = paginator.page(page)
    except PageNotAnInteger:
        receitas = paginator.page(1)
    except EmptyPage:
        receitas = paginator.page(paginator.num_pages)
    return render(request, 'registration/adicionar_receita.html', {'form': form, 'receitas': receitas})

def delete_receita(request, receita_id):
    receita = Receita.objects.get(pk=receita_id)
    receita.delete()
    return redirect('adicionar_receita')

@login_required
def calcular_porcentagem_categoria(usuario):
    categorias = Despesa.objects.all()
    porcentagens = {}
    total_despesas = Despesa.objects.filter(usuario=usuario).aggregate(Sum('valor'))['valor__sum'] or 0

    for categoria in categorias:
        valor_categoria = Despesa.objects.filter(usuario=usuario, categoria=categoria).aggregate(Sum('valor'))['valor__sum'] or 0
        porcentagem = (valor_categoria / total_despesas) * 100 if total_despesas > 0 else 0
        porcentagens[categoria.nome] = round(porcentagem, 2)

    return porcentagens

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

    paginator = Paginator(despesas, 5) 
    page = request.GET.get('page')

    try:
        despesas = paginator.page(page)
    except PageNotAnInteger:
        despesas = paginator.page(1)
    except EmptyPage:
        despesas = paginator.page(paginator.num_pages)

    return render(request, 'registration/adicionar_despesa.html', {'form': form, 'despesas': despesas})

def delete_despesa(request, despesa_id):
    despesa = Despesa.objects.get(pk=despesa_id)
    despesa.delete()
    return redirect('adicionar_despesa')

