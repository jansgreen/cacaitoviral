from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.


class AccionesYutube(models.Model):
    """
    estos son los campos que usaremos para almacenar las vias.
    """
    class Meta:
        verbose_name_plural = 'AccionesYutube'
    Id_Canal = models.CharField(max_length=355, null=True, editable=True)
    Id_Video = models.CharField(max_length=355, null=True, editable=True)
    thumbnails =  models.URLField(max_length=200, default=True)
    Titulo = models.CharField(max_length=355, null=True, editable=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comentar = models.IntegerField(null=True, editable=True, default=0)
    segundos = models.IntegerField(null=True, editable=True, default=25)
    repetir = models.IntegerField(null=True, editable=True, default=1)
    compartir = models.IntegerField(null=True, editable=True, default=0)
    Me_Gusta =  models.IntegerField(null=True, editable=True, default=0)
    Suscripcion = models.IntegerField(null=True, editable=True, default=0)

    
    def __str__(self):
        return str(self.Id_Video)

