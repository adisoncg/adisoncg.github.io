from django.shortcuts import render, redirect
from .models import Meta
from .forms import MetaForm 

def metas(request):
    if request.method == 'POST':
        form = MetaForm(request.POST)
        if form.is_valid():
            nova_meta = form.save(commit=False)
            nova_meta.usuario = request.user
            nova_meta.save()

    else:
        form = MetaForm() 

    metas = Meta.objects.filter(usuario=request.user)
    return render(request, 'registration/metas.html', {'metas': metas, 'form': form})
