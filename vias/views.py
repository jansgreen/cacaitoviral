import requests
# YOUTUBE API IMPORT
import os
import sys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


from  isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import YoutubeForms
from .models import AccionesYutube
from .quickstart import main
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Q
# YOUTUBE API
#from google_auth_oauthlib.flow import Flow
from google_auth_oauthlib.flow import InstalledAppFlow

#================================#
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

#=========================================#

#YOUTUBE SCOPLES

YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

# Disable OAuthlib's HTTPS verification when running locally.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

CLIENT_SECRETS_FILE = "client_secrets_file.json"

# Get credentials and create an API client
SCOPES = ["https://www.googleapis.com/auth/youtube",
          "https://www.googleapis.com/auth/youtube.force-ssl",
          "https://www.googleapis.com/auth/youtubepartner"]



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
    search_url = UrlMain.search_url
    video_url = UrlMain.video_url
    videos = []
    video_ids = []
    youtube_list = AccionesYutube.objects.all()

    buscar = request.GET.get("buscador")
    if buscar:
        params = {
            'part': 'snippet',
            'q' : buscar,
            'key': settings.API_KEY_YOUTUBE,
            'type': 'video',
        }
    else:
        for Title in youtube_list:
            params = {
                'part': 'snippet',
                'q' : Title,
                'key': settings.API_KEY_YOUTUBE,
                'type': 'video',
            }
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
    paginator = Paginator(youtube_list, 20)
    Coordenadas = "Coordenadas"
    template = 'index/Mapa.html'
    if paginator:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'Coordenadas': Coordenadas,
            }
        return render(request, 'index/Mapa.html', context)
    return render(request, template, context)


def selecionado(request, video_id):
    form = YoutubeForms()
    Vias_Id = AccionesYutube.objects.filter(Q(Id_Video__icontains = video_id))
    if Vias_Id:
        messages.warning(request, f'Ya existe una via con este video, Selecione otro video o actualice el existente')
        return redirect('agregar_via')
    else:
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
        form = YoutubeForms(request.POST, request.FILES)
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

            
 
def pasos(request, Id_Video, **args):
    via = AccionesYutube.objects.filter(Q(Id_Video__icontains = Id_Video))
    template = "index/pasos.html"
    context = {
        'via': via,
        'video':Id_Video,
    }
    return render (request, template, context)


def get_authenticated_service(request, **args): # Modified
    credential_path = os.path.join('./', 'credential_sample.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, SCOPES)
        credentials = run_flow(flow, store)
    return build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

def Youtube_like(request, video):
    """Update video rating (use 'none' to unset)"""
    main()
    print(auth)
    rating="like"

    return youtube.videos().rate(id=video, rating=rating).execute()
