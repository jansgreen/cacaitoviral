from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name='index'),
    path('via/', views.agregar_via, name='agregar_via'),
    path('Listar/', views.Listar, name='Listar'),
    path('Mapa/', views.Mapa, name='Mapa'),
    path('selecionado/(?P<video_id>[^/]+)$', views.selecionado, name='selecionado'), 
    path('Crear_via/', views.Crear_via, name='Crear_via'),
    path('pasos/<str:Id_Video>', views.pasos, name='pasos'),
    path('Youtube_like/<str:video>', views.Youtube_like, name='Youtube_like'),
    path('get_authenticated_service', views.get_authenticated_service, name='get_authenticated_service'),


    ]



