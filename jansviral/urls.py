"""jansviral URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vias.views import index, agregar_via, Listar
from perfiles.views import registro

from django.conf import settings
from django.conf.urls.static import static

### CORRESPONDE A VIAS APP
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('via', agregar_via, name='agregar_via'),
    path('Listar', Listar, name='Listar'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

### CORRESPONDE A PERFILES APP
urlpatterns += [
    path('registro', registro, name='registro'),

]

urlpatterns += [
    path('accounts/', include('allauth.urls')),
]

