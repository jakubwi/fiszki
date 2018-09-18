from django import forms
from django.contrib.auth.models import User
from .models import Deck, Card

class CardForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    front = forms.CharField(widget=forms.Textarea)
    back = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Card
        exclude = ('deck', 'author' )