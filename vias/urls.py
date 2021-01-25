from django.urls import path
from . import views



urlpatterns =[
    path('', views.index, name='index'),
    path('via/', views.agregar_via, name='agregar_via'),
    path('Listar/', views.Listar, name='Listar'),
    path('Mapa/', views.Mapa, name='Mapa'),
    path('selecionado/<str:video_id>', views.selecionado, name='selecionado'), 
    path('Crear_via/', views.Crear_via, name='Crear_via'),


    ]

