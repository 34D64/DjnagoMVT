from django.forms import ModelForm,forms
from django import forms
from .models import Music

class musicForm(ModelForm):
    title = forms.CharField()
    title1 = forms.CharField()
    title2 = forms.CharField()
    title3 = forms.CharField()
    title4 = forms.CharField()
    title5 = forms.CharField()
    title6 = forms.CharField()
    class Meta:
        model = Music
        fields = "__all__"
        # fields = ['Artist','Name','cover']
    