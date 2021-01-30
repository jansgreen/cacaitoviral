from django.contrib import admin
from .models import AccionesYutube
from embed_video.admin import AdminVideoMixin

# Register your models here.


class AccionesYutubeAdmin(admin.ModelAdmin):
    fields = (
        'user',
        'Id_Video',
        'thumbnails',
        'Titulo',
        'segundos',
        'repetir',
        'comentar',
        'compartir',
        'Me_Gusta',
        'Suscripcion',
    )
    list_display =(
        'pk',
        'user',
        'Id_Video',
        'thumbnails',
        'Titulo',
        'segundos',
        'repetir',
        'comentar',
        'compartir',
        'Me_Gusta',
        'Suscripcion',
    )


       
admin.site.register(AccionesYutube, AccionesYutubeAdmin)
