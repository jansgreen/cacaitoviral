from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto =  models.ImageField(upload_to="ImagenVia", null=True, default=f'{User.username}.png')
    telefono = models.CharField(max_length=20, null=True, editable=True)
    Direccion = models.CharField(max_length=250, null=True, editable=True)
    

    def __str__(self):
        return f'{self.user.username}'



