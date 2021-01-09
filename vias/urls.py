from django.urls import path
from . import views



urlpatterns =[
    path('', views.index, name='index'),
    path('via/', views.agregar_via, name='agregar_via'),
    path('Listar/', views.Listar, name='Listar'),
    ]

