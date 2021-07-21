from django import forms
from  .models import News


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body']

class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'body']