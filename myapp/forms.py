from dataclasses import field, fields
from django import forms
from . models import Musician,Album

class MusicianForms(forms.ModelForm):
    class Meta:
        model=Musician
        fields="__all__"

class AlbumForms(forms.ModelForm):
    class Meta:
        model=Album
        fields="__all__"