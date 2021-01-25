from django import forms
from .widgets import CustomClearableFileInput
from .models import Vias, Tipo, AccionesYutube
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
        attr = ['type', 'class']
        for attrx in attr:
            self.fields['accion'].widget.attrs[attrx] = 'checkbox'
            self.fields['accion'].widget.attrs[attrx] = 'bg-prymary'



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



OpcionesYutube = [
    ('comentar', 'Comentar'),
    ('reproducion', 'Reproduccion'),
    ('compartir', 'Compartir'),
    ('meGusta', 'Me Gusta'),

]

class YoutubeVia(forms.ModelForm):
    class Meta:
        model = AccionesYutube
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.fields['Titulo'] or self.fields['Video_ID']:
                self.fields[field].widget.attrs['type'] = 'text'
            elif self.fields['reproducion']:
                self.fields[field].widget.attrs['type'] = 'checkbox'
            elif self.fields['YoutubeUser']:
                self.fields[field].widget.attrs['type'] = 'hidden'
            else:
                self.fields[field].widget.attrs['type'] = 'number'
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['aria-label'] = 'Sizing example input'
            self.fields[field].widget.attrs['aria-describedby'] = 'basic-addon2'
            self.fields[field].label = False

