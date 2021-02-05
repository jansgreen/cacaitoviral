from django.shortcuts import render, redirect
from .forms import UserPersonalizado, PerfilPersonalizado, LoginPersonalizado
from django.contrib.auth import authenticate, login




# Create your views here.

def fedd(request):
    return render(request, 'social/feed.html')

def registro(request):
    if request.method == 'POST':
        return redirect('Mapa')
    data ={
        'form':UserPersonalizado,
        'ext_form': PerfilPersonalizado,
        'aside_Rigth': 'aside_Rigth',
        
    }
    return render(request, 'account/signup.html', data)

def iniciar(request):
    aside_Rigth = "aside_Rigth"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('Mapa')

    context ={
        'form':LoginPersonalizado,
        'aside_Rigth':aside_Rigth,
    }
    return render(request, 'account/login.html', context)

def politica(request):
    return render(request, "politica.html")
