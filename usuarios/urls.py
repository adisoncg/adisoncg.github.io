from django.urls import path, include
from . import views


urlpatterns = [
    
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('financeiro/', include('financeiro.urls')),
    path('metas/', include('metas.urls')),
    path('autenticacao/', include('autenticacao.urls')),
]
