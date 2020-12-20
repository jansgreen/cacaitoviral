from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

path('/', views.index, name='index'),
path('via', views.agregar_via, name='agregar_via'),


if settings.DEBUG:
    urlpetterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

