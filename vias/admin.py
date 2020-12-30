from django.contrib import admin
from .models import Vias, Tipo, Accion

# Register your models here.

class AccionAdmin(admin.ModelAdmin):
    """
    mostrar los campos del model en el admin de django
    """
    fields=(
        'accion',
        'precio',
        )
    list_display = (
        'accion',
        'precio',

    )


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
        'accion', 
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

admin.site.register(Accion, AccionAdmin)
admin.site.register(Vias, ViasAdmin)
admin.site.register(Tipo, TiposAdmin)