from django.shortcuts import render
from .forms import UserPersonalizado, PerfilPersonalizado



# Create your views here.


def registro(request):
    data ={
        'form':UserPersonalizado,
        'ext_form': PerfilPersonalizado,
    }
    return render(request, 'account/signup.html', data)
