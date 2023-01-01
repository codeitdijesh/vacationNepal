from django import forms
from .models import Packages

class Packageform(forms.ModelForm):
    class Meta:
        model=Packages
        fields='__all__'

