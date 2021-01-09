from django.shortcuts import render
from .forms import UserPersonalizado, PerfilPersonalizado
from django.views.generic import TemplateView



# Create your views here.

def fedd(request):
    return render(request, 'social/feed.html')

def registro(request):
    return render(request, 'account/signup.html')


"""
def registro(request):
    data ={
        'form':UserPersonalizado,
        'ext_form': PerfilPersonalizado,
    }
    return render(request, 'account/signup.html', data)

    """
