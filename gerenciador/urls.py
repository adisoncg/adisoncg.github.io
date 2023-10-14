from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('dashboard') if request.user.is_authenticated else redirect('login'), name='home'),
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')), 
    path('financeiro/', include('financeiro.urls')),
    path('metas/', include('metas.urls')),
    path('autenticacao/', include('autenticacao.urls')),

]
