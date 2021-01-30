from django import forms
from .widgets import CustomClearableFileInput
from .models import AccionesYutube
from django.contrib.auth.models import User



class YoutubeForms(forms.ModelForm):
    class Meta:
        model = AccionesYutube
        fields = '__all__' 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            if self.fields['Titulo']: #or self.fields['Video_ID']:
                self.fields[field].widget.attrs['type'] = 'text'
            elif self.fields['user']:
                self.fields[field].widget.attrs['type'] = 'hidden'
            else:
                self.fields[field].widget.attrs['type'] = 'number'
            self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].widget.attrs['aria-label'] = 'Sizing example input'
            self.fields[field].widget.attrs['aria-describedby'] = 'basic-addon2'
            self.fields[field].label = False

