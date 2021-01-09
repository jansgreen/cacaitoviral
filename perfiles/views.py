from django.shortcuts import render
from .forms import UserPersonalizado, PerfilPersonalizado, LoginPersonalizado



# Create your views here.

def fedd(request):
    return render(request, 'social/feed.html')

def registro(request):
    data ={
        'form':UserPersonalizado,
        'ext_form': PerfilPersonalizado,
        'aside_Rigth': 'aside_Rigth',
        
    }
    return render(request, 'account/signup.html', data)

def iniciar(request):
    data ={
        'form':LoginPersonalizado,
        'aside_Rigth':'aside_Rigth',
       
    }
    return render(request, 'account/login.html', data)
