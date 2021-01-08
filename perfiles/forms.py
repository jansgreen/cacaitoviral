from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserPersonalizado(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username',
        ]
    print(UserCreationForm)
    pass
    
    

class PerfilPersonalizado(forms.ModelForm):
    class Meta:
        model = Profile

        exclude = ['user']
        fields = [
        'foto',
        'telefono',
        'Direccion',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'foto': 'Por favor suba su foto de perfil',
            'telefono': 'Ingrese su numero de telefono',
            'Direccion': 'Ingrese su direcion de vivienda',
            }

        self.fields['foto'].widget.attrs['autofocus'] = True
    
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


