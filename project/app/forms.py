from django import forms
from .models import AppModel

class AppForm(forms.ModelForm):

    token = forms.CharField(label="OAuth-токен", max_length=65)
    public_key = forms.CharField(label="public_key",max_length=100)
    class Meta:
        model = AppModel
        fields = "__all__"
        
    