from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from usuarios.views import dashboard
from . import views

urlpatterns = [
        path('registro/', views.register, name='registro'),  
        path('accounts/', include('django.contrib.auth.urls')),
        path('dashboard/', dashboard, name='dashboard'),
]

