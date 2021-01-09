from django.contrib.auth.models import User
from .models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginPersonalizado(AuthenticationForm):
    class Meta:
        model = User
        fields = [
        'username',
        'password',
        ]
        


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        password = forms.CharField(widget=forms.PasswordInput())
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['type'] ='password'

        self.fields['username'].label = False
        self.fields['password'].label = False

  
    

class PerfilPersonalizado(UserCreationForm):
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



class UserPersonalizado(UserCreationForm):
    class Meta:
        model = User
        fields = [
        'username',
        'password1',
        'password2',
        'email',
        'first_name',
        'last_name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'username': 'Escriba su nombre de usuario',
            'password1': 'Escriba su contraseña',
            'password2': 'Confirmemos su contraseña',
            'email': 'Espesifique su correo electronico',
            'first_name': 'Ingrese su primer Nombre',
            'last_name': 'Ingrese su apellido',

            }

        self.fields['username'].widget.attrs['autofocus'] = True
        self.fields['password1'].widget.attrs['type'] ='password'
        self.fields['password2'].widget.attrs['type'] ='password'
    
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


