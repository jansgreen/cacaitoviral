from django.shortcuts import render, get_object_or_404, reverse
from .forms import TiposForm, ViasForm
from .models import Vias
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .youtube_API import Youtube




# Create your views here.
def index(request):
    """
    muestra la pagina princiapl
    """
    #Youtube()
    return render(request, 'index/index.html')


def agregar_via(request):
    """
    esta funcion es para agregar las vias; solo puede agregar una por una
    """
    #check_vias = Vias.objects.get.all().order_by('link')
    user = User.objects.get()
    if request.method == 'POST':
        form = ViasForm(request.POST, files=request.FILES) #initial={'user': request.user.id}
        in_form_link = form['link'].value()
        in_form_name = form['nombre_via'].value()
        if form:
            filter_via = Vias.objects.filter(Q(link__icontains = in_form_link)).distinct()
            if filter_via:
                messages.warning(request, f'Usted ya tiene una esta via con el nombre {in_form_name}')
            else:
                if form.is_valid():
                    form_user = form.save(commit=False)
                    form_user.usuario = request.user  # The logged-in user
                    form.save()
                    messages.success(request, 'Su via ha sido guardada exitosamente.')
                    return HttpResponseRedirect(reverse('agregar_via'))
                else:
                    messages.debug(request, f'Ocurrio un error, esto no pudo haber pasado contacta al administrador.')
    else:
        form = ViasForm()
    template = 'index/agregar_via.html'
    context = {
        'form': form,

    }
    return render(request, template, context)

# LISTAR LAS VIAS

def Listar(request):
    Listar_vias = Vias.objects.get.all()
    Current_User = request.user
    template = 'index/escritorio.html'
    context = {
        'Listar_vias': Listar_vias,
    }
    return render(request, template, context)  


    
        