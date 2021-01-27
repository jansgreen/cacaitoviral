import requests

from  isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, get_object_or_404, reverse
from .forms import TiposForm, ViasForm, YoutubeVia
from .models import Vias, AccionesYutube
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from .youtube_API import Youtube




class UrlMain:
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'


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
    buscar = request.GET.get("buscador")
    search_url = UrlMain.search_url
    video_url = UrlMain.video_url
    video_ids = []
    videos = []

    params = {
        'part': 'snippet',
        'q' : buscar,
        'key': settings.API_KEY_YOUTUBE,
        'type': 'video',
    }
    video_ids = []
    r = requests.get(search_url, params=params)
    resultados = r.json()['items']
    for resultado in resultados:
        video_ids.append(resultado['id']['videoId'])
    
    video_params = {
        'key' : settings.API_KEY_YOUTUBE,
        'part': 'snippet,contentDetails',
        'id': ','.join(video_ids)
    }

    v = requests.get(video_url, params=video_params)
    video_resultados = v.json()['items']
    for video in video_resultados:
        datos_videos ={
            'Id_Canal': video['snippet']['channelId'],
            'Titulo': video['snippet']['title'],
            'Id_Video': video['id'],
            'Duracion': parse_duration(video['contentDetails']['duration']).total_seconds(),
            'thumbnails': video['snippet']['thumbnails']['high']['url'],
        }

        videos.append(datos_videos)

    template = 'index/buscador.html'
    context = {
        'videos': videos,
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

def Mapa(request):
    
    youtube_list = AccionesYutube.objects.all()
    Coordenadas = "Coordenadas"
    template = 'index/Mapa.html'
    context = {
        'youtube_list': youtube_list,
        'Coordenadas': Coordenadas,
    }
    return render(request, template, context)


def selecionado(request, video_id):
    form = YoutubeVia()
    videos =[]
    url = UrlMain.video_url
    video_params = {
        'key' : settings.API_KEY_YOUTUBE,
        'part': 'snippet,contentDetails',
        'id': video_id
    }
    v = requests.get(url, params=video_params)
    video_resultados = v.json()['items']
    for video in video_resultados:
        datos_videos ={
            'Id_Canal': video['snippet']['channelId'],
            'Titulo': video['snippet']['title'],
            'Id_Video': video['id'],
            'Duracion': parse_duration(video['contentDetails']['duration']).total_seconds(),
            'thumbnails': video['snippet']['thumbnails']['high']['url'],
        }

        videos.append(datos_videos)
    template = 'index/buscador.html'
    context = {
        'videos': videos,
        'form': form,
        }   
    return render(request, 'index/selecionado.html', context)

def Crear_via(request):
    if request.method == 'POST':
        checkbox = request.GET.get('Reproducir')
        form = YoutubeVia(request.POST, request.FILES)
        if form:
            if form.is_valid():
                form_user = form.save(commit=False)
                form_user.usuario = request.user
                form.save()
                messages.success(request, 'Su via se ha creado exitosamente.')
                return HttpResponseRedirect(reverse('agregar_via'))

            else:
                messages.debug(request, f'Ocurrio un error, esto no pudo haber pasado contacta al administrador.')
                return HttpResponseRedirect(reverse('agregar_via'))
        else:
            messages.debug(request, f'Ocurrio un error, esto no pudo haber pasado contacta al administrador.')
            return HttpResponseRedirect(reverse('agregar_via'))
    else:
        messages.debug(request, f'Accesso Denegado.')
        return HttpResponseRedirect(reverse('Mapa'))

            
 



#    if request.method == 'POST':
#        form = ViasForm(request.POST, files=request.FILES) #initial={'user': request.user.id}
#        in_form_link = form['link'].value()
#        in_form_name = form['nombre_via'].value()
#        if form:
#            filter_via = Vias.objects.filter(Q(link__icontains = in_form_link)).distinct()
#            if filter_via:
#                messages.warning(request, f'Usted ya tiene una esta via con el nombre {in_form_name}')
#            else:
#                if form.is_valid():
#                    form_user = form.save(commit=False)
#                    form_user.usuario = request.user  # The logged-in user
#                    form.save()
#                    messages.success(request, 'Su via ha sido guardada exitosamente.')
#                    return HttpResponseRedirect(reverse('agregar_via'))
#                else:
#                    messages.debug(request, f'Ocurrio un error, esto no pudo haber pasado contacta al administrador.')


    
        