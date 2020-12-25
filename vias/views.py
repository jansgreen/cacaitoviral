from django.shortcuts import render, get_object_or_404, reverse
from .forms import TiposForm, ViasForm
from .models import Vias
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect



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
    user = User.objects.get()
    print(request.user.id)
    if request.method == 'POST':
        form = ViasForm(request.POST, files=request.FILES, initial={'user': request.user.id})
        if form.is_valid():
            form_user = form.save(commit=False)
            form_user.usuario = request.user  # The logged-in user
            form.save()
            messages.success(request, 'Su via ha sido guardada exitosamente.')
            return HttpResponseRedirect(reverse('agregar_via'))

        else:
            print("aqui hay un error")
    else:
        form = ViasForm()
    template = 'index/agregar_via.html'
    context = {
        'form': form,

    }
    return render(request, template, context)

