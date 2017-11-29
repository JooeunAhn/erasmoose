from django import forms

from .models import Moose
from .widgets import GoogleMapPointWidget


class MooseForm(forms.ModelForm):
    class Meta:
        model = Moose
        fields = ['latlng', 'description', 'image',]
        widgets = {
            'latlng': GoogleMapPointWidget,
        }