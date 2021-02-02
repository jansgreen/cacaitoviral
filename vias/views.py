import requests
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import httplib2
import os
import sys

from  isodate import parse_duration

from django.conf import settings
from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import YoutubeForms
from .models import AccionesYutube
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.db.models import Q
# YOUTUBE API
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow




YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


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
        print(url)
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
#    like_video()
    template = "index/pasos.html"
    context = {
        'via': via,
        'video':Id_Video,
    }
    return render (request, template, context)

CLIENT_SECRETS_FILE = "client_secret.json"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" 
   
scopes = ["https://www.googleapis.com/auth/youtube",
            "https://www.googleapis.com/auth/youtube.force-ssl",
            "https://www.googleapis.com/auth/youtubepartner"]

def get_authenticated_service():
#    flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE, scope=YOUTUBE_READ_WRITE_SCOPE, message=MISSING_CLIENT_SECRETS_MESSAGE)
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes)
    storage = None
    credentials = run_flow(flow, storage)


    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, http=credentials.authorize(httplib2.Http()))

def Youtube_like(request, video):
    if video:
        get_authenticated_service()

    youtube.videos().rate(
        id=video,
        rating="like"
    ).execute()

    return HttpResponseRedirect(reverse('Mapa'))