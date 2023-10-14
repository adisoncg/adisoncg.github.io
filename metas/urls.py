from django.urls import path
from . import views

urlpatterns = [
    path("metas/", views.metas, name='metas'),
]
