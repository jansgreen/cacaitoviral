from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    path('registro/', views.registro, name='registro'),
    path('iniciar/', views.iniciar, name='iniciar'),
    path('politica/', views.politica, name='politica')

    ]
