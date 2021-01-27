from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class Accion(models.Model):
    """
    Tipos de vias disponible, una varias vias pueden perteneser solamente a un tipo
    """
    accion = models.CharField(max_length=20, null=True, editable=True)
    precio = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return str(self.accion)

class Tipo(models.Model):
    """
    Tipos de vias disponible, una varias vias pueden perteneser solamente a un tipo
    """
    tipo_via = models.CharField(max_length=20, null=True, editable=True)

    def __str__(self):
        return str(self.tipo_via)


class Vias(models.Model):
    """
    estos son los campos que usaremos para almacenar las vias.
    """
    class Meta:
        verbose_name_plural = 'Vias'

    nombre_via = models.CharField(max_length=20, null=True, editable=True)
    link = models.CharField(max_length=100, null=True, editable=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    imagen =  models.ImageField(upload_to="ImagenVia", null=True)
    fecha = models.DateField(default=datetime.date.today)
    accion = models.ManyToManyField(Accion, blank=True)


    
    def __str__(self):
        return str(self.nombre_via)

class AccionesYutube(models.Model):
    """
    estos son los campos que usaremos para almacenar las vias.
    """
    class Meta:
        verbose_name_plural = 'Acciones'
    Id_Video = models.CharField(max_length=355, null=True, editable=True)
    thumbnails =  models.URLField(max_length=200, default=True)
    Titulo = models.CharField(max_length=355, null=True, editable=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    comentar = models.IntegerField(null=True, editable=True, default=0)
    reproducion = models.BooleanField(default=False)
    compartir = models.IntegerField(null=True, editable=True, default=0)
    Me_Gusta =  models.IntegerField(null=True, editable=True, default=0)
    Suscripcion = models.IntegerField(null=True, editable=True, default=0)


    
    def __str__(self):
        return str(self.Titulo)
