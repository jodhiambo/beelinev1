from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .countries import COUNTRIES
from django.core.files import File
from PIL import Image
from django import forms
from challengegov import settings


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username','email',)
