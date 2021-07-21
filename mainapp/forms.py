from django import forms
from .models import Preapproved_challenge, ChallengeTag, STATUS, Challenges

class ChallengesModelForm(forms.ModelForm):
    class Meta:
        model = Challenges
        fields = ('status',)
        widgets = {
            'status': forms.Select(choices=STATUS)
        }


class CreatePreapprovedChallengeForm(forms.ModelForm):
    steps_to_complete = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"List each step in detail"}))
    why = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Type Why People should take your Challenge (Optional)"}), required=False)
    tips = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"The hints that make this Challenge work (Optional)"}), required=False)
    length = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"How many days would you like the Challenge to run"}))
    external_url = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Enter the link to the challenge or somewhere we can get more information"}))
    tags = forms.ModelMultipleChoiceField(widget=forms.SelectMultiple,label="Tags: <span style='font-size:11px!important;font-fammily:'Gilroy''>Hold down 'Control', or 'Command' on a Mac, to select more than one.</span>", queryset=ChallengeTag.objects.all())
    class Meta:
        model = Preapproved_challenge
        fields = '__all__'
