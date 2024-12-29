from django import forms
from . import models


class MusicianForms(forms.ModelForm):
    class Meta:
        model=models.Musician_Model
        fields='__all__'

