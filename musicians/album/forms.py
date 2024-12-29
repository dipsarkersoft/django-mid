from django import forms
from . import models


class AlbumForms(forms.ModelForm):
    class Meta:
        model=models.Album_model
        fields='__all__'


