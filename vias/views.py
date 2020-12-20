from django.shortcuts import render
from .forms import TiposForm, ViasForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def index(request):
    """
    muestra la pagina princiapl
    """
    return render(request, 'index/index.html')


def agregar_via(request):
    """
    esta funcion es para agregar las vias; solo puede agregar una por una
    """
    if request.method == 'POST':
        form = ViasForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile update successfully')
        else:
            messages.error (request, 'Update failed. Please ensure the form is valid.')
    else:
        form = ViasForm()
    template = 'index/agregar_via.html'
    context = {
        'form': form,

    }
    return render(request, template, context)
