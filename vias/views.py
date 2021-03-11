import requests
# YOUTUBE API IMPORT
import os
import sys
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client import tools # Added



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
from googleapiclient.discovery import build
#from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

#=========================================#

#YOUTUBE SCOPLES
YTB = build('youtube', 'v3', developerKey=settings.API_KEY_YOUTUBE)
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
    get_rating = 'https://www.googleapis.com/youtube/v3/videos/getRating'
    Auth_permiso = 'https://accounts.google.com/o/oauth2/auth?'

class Auth:
    def Auths():
        Auth_Url = UrlMain.Auth_permiso
        Auth_params = {
        'client_id' : settings.YOUTUBE_CLIENT_ID,
        'redirect_uri': 'http://127.0.0.1:8000/accounts/google/login/callback/',
        'SCOPES':SCOPES,
        'response_type': 'code&',
        'access_type': 'offline',
    }
    
        v = requests.get(Auth_Url, params=Auth_params)
        print(v)

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
        r = requests.get(search_url, params=params)
        resultados = r.json()
        for resultado in resultados['items']:
            video_ids.append(resultado['id']['videoId'])
        video_params = {
            'key' : settings.API_KEY_YOUTUBE,
            'part': 'snippet,contentDetails',
            'id': ','.join(video_ids)
        }
    else:
        for Vias_video_id in youtube_list:
            video_ids.append(Vias_video_id)
        video_params = {
            'key' : settings.API_KEY_YOUTUBE,
            'part': 'snippet,contentDetails',
            'id': video_ids
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
    auth_access = UrlMain.Auth_permiso
    via = AccionesYutube.objects.filter(Q(Id_Video__icontains = Id_Video))
    get_rating_var = UrlMain.get_rating
    params = {
        'id': Id_Video,
        }
    Auth_params = {
        'client_id' : settings.YOUTUBE_CLIENT_ID,
        'redirect_uri': 'http://127.0.0.1:8000/accounts/google/login/callback/',
        'SCOPES':SCOPES,
        'response_type': 'code&',
        'access_type': 'offline',
    }
    v = requests.get(get_rating_var, params=params)
    #================================Credentials=====================================
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, scopes=SCOPES)
    flow.run_local_server(port=8080, prompt="consent")
    credentials = flow.credentials
    print(credentials.json())
    A = requests.post(auth_access, params=Auth_params)
    raiting_boolean = v.json()
    test = get_authenticated_service
    print("============= CALIFICACION DEL VIDEO ===========================")
    test
    print("========================================")
    
    template = "index/pasos.html"
    context = {
        'via': via,
        'video':Id_Video,
    }
    return render (request, template, context)


def get_authenticated_service(): # Modified
    print('Funcion de Auth')
    credential_path = os.path.join('./', 'client_secrets_file.json')
    flow = InstalledAppFlow.from_clients_secrets_file(credential_path, SCOPES)
    print(flow)
    credentials = flow.run_local_server(port=8080)#run_flow(flow, store)
    print('Not Credentials')
    print('Funcion de Auth 2')
    return build(API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=credentials)

def Youtube_like(request, video):
    """Update video rating (use 'none' to unset)"""


    return youtube.videos().rate(id=video, rating=rating).execute()
