from django import forms
from .widgets import CustomClearableFileInput
from .models import Vias, Tipo
from django.contrib.auth.models import User




class TiposForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = '__all__'

    Tipo_nombre = forms.CharField(widget=forms.TextInput())


class ViasForm(forms.ModelForm):
    class Meta:
        model = Vias
        exclude = ['usuario', ]
        fields = [
        'nombre_via',
        'link',
        'tipo',
        'imagen',
        'fecha',
        'accion',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'nombre_via': 'Nombre de la Via',
            'link': 'Link de la via',
            'fecha': 'Fecha',
            'imagen': 'sube la imagen',
            'tipo': 'Fecha',
            'accion': 'seleciona lo que quieres que se haga en tu via',

            }

        self.fields['nombre_via'].widget.attrs['autofocus'] = True
    
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['type'] = 'text'
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['aria-label'] = 'Sizing example input'
            self.fields[field].widget.attrs['aria-describedby'] = 'basic-addon2'
            self.fields[field].label = False