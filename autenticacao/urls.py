from django.urls import path
from django.contrib.auth import views as auth_views
from usuarios.views import dashboard
from . import views

urlpatterns = [
        path('registro/', views.register, name='registro'),  
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('dashboard/', dashboard, name='dashboard'),
]

