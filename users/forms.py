from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import GuideInfo



class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email' ,'password1', 'password2']
       

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for  name,field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class Guideform(forms.ModelForm):
    class Meta:
        model=GuideInfo
        fields = "__all__"
        exclude = ('user','approvedByAdmin',)

     
    def __init__(self, *args, **kwargs):
        super(Guideform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})           

            