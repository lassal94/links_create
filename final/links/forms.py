from django import forms
from .models import Links

class AddLinks(forms.ModelForm):
    full_url = forms.CharField(
        label="Длинная ссылка",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    short_url = forms.CharField(
        label="Короткая ссылка",
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Links
        fields = ['full_url', 'short_url']

