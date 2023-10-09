from django.urls import path
from . import views
from usuarios.views import dashboard

urlpatterns = [
    path('adicionar_receita/', views.adicionar_receita, name='adicionar_receita'),
    path('adicionar_despesa/', views.adicionar_despesa, name='adicionar_despesa'),
    path('delete_despesa/<int:despesa_id>/', views.delete_despesa, name='delete_despesa'),
    path('delete_receita/<int:receita_id>/', views.delete_receita, name='delete_receita'),
    path('dashboard/', dashboard, name='dashboard'),
]
