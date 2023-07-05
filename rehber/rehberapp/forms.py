from django import forms
from .models import Kisi,Sirket

class KisiForm(forms.ModelForm):
    class Meta:
        model = Kisi
        fields = ['adsoyad', 'tel', 'email', 'sirket']

class SirketForm(forms.ModelForm):
    class Meta:
        model = Sirket
        fields = ['isim', 'adres', 'tel', 'email','web']
