from django import forms
from .models import CryptoApi

class CryptoApiForm(forms.ModelForm):
    class Meta:
        model = CryptoApi
        fields = "__all__"
        labels = {
            'slug' : 'Entrez votre crypto ici',
            'convert' : 'Entrez votre devise ici'
        }