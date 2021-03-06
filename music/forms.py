from django.contrib.auth.models import User
from django import forms
from .models import Album, Song

class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']
