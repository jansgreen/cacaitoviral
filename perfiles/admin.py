from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    fields=(
        'user',  
        'foto',
        'telefono', 
        'Direccion',
        )
    list_display = (
    'user',  
    'foto',
    'telefono', 
    'Direccion',
    )

admin.site.register(Profile, ProfileAdmin)
