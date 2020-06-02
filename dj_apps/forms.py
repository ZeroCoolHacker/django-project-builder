from django import forms
from .models import Dj_App

class AppForm(forms.ModelForm):
    
    class Meta:
        model = Dj_App
        fields = '__all__'