from django.contrib import admin
from .models import Vias, Tipo

# Register your models here.

class ViasAdmin(admin.ModelAdmin):
    """
    mostrar los campos del model en el admin de django
    """
    fields=(
        'nombre_via',
        'link',
        'tipo',
        'usuario',
        'imagen',
        'fecha', 
        )
    list_display = (
        'nombre_via',
        'link',
        'tipo',
        'usuario',
        'imagen',
        'fecha',

    )

class TiposAdmin(admin.ModelAdmin):
    fields = (
        'tipo_via',
    )
    list_display =(
        'pk',
        'tipo_via',
    )


admin.site.register(Vias, ViasAdmin)
admin.site.register(Tipo, TiposAdmin)