from django import forms
from users.countries import COUNTRIES
from .models import Profile
from users.models import CustomUser
from imagekit.forms import ProcessedImageField
from imagekit.processors import ResizeToFill


class ProfileUpdateForm(forms.ModelForm):

    nationality = forms.Select(choices=COUNTRIES)
    country_of_residence = forms.Select(choices=COUNTRIES)
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={"placeholder":"Klaus"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={"placeholder":"Mikaelson"}))
    organization = forms.CharField(label='Organization', widget=forms.TextInput(attrs={"placeholder":"The Originals Organization"}))
    consent_to_share_my_information = forms.CheckboxInput()
    consent_to_view_my_bookmarks = forms.CheckboxInput()
    # photo = ProcessedImageField(
    #     spec_id='userprofile:profile:photo',
    #     label=('Profile Photo'),
    #     processors=[ResizeToFill(100,100)],
    #     format='JPEG',
    #     options={'quality':60},
    #     required=False,
    #     error_messages = {'invalid':("Image files only")}, widget=forms.FileInput)

    class Meta:
        model = Profile
        username = None
        fields = [ 
            # 'photo', 
            'first_name', 'last_name', 'organization', 'nationality', 'country_of_residence', 'age_group', 'sex', 'consent_to_share_my_information', 'consent_to_view_my_bookmarks']
