from django import forms
from .widgets import CustomClearableFileInput
from .models import Vias, Tipos
from django.contrib.auth.models import User


class TiposForm(forms.ModelForm):
    class Meta:
        model = Tipos
        fields = '__all__'

    Tipo_nombre = forms.CharField(widget=forms.TextInput())


class ViasForm(forms.ModelForm):
    class Meta:
        model = Vias
        fields = (
        'nombre_via',
        'link',
        'tipo',
        'usuario',
        'imagen',
        'fecha',
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'nombre_via': 'Nombre de la Via',
            'link': 'Link de la via',
            'imagen': 'sube la image que tendra la via',
            'fecha': 'Fecha',
            'tipo': 'Fecha',
            'usuario': 'usuario',
            }
        self.fields['nombre_via'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            if field == 'imagen':
                self.fields[field].widget.attrs['class'] = 'btn btn-primary'
                self.fields[field].widget.attrs['id'] = 'button-addon1'
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['type'] = 'text'
                self.fields[field].widget.attrs['aria-label'] = 'Sizing example input'
                self.fields[field].widget.attrs['aria-describedby'] = 'basic-addon2'
                self.fields[field].label = False
            else:
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs['type'] = 'text'
                self.fields[field].widget.attrs['class'] = 'form-control'
                self.fields[field].widget.attrs['aria-label'] = 'Sizing example input'
                self.fields[field].widget.attrs['aria-describedby'] = 'basic-addon2'
                self.fields[field].label = False



        tipos_form = Tipos.objects.all()
        name = [(c.id, c.tipo_via) for c in tipos_form ]
        if self.fields['tipo']:
            self.fields['tipo'].choices = name
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] =  'border-black rounded-0'