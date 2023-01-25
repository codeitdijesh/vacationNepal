from django import forms
from .models import Packages



# class Packageform(forms.ModelForm):
#     class Meta:
#         model=Packages
#         fields=['packageName','price','packageDuration','description','isUnderRated']
#         widgets = {
#            'packageName':forms.TextInput(attrs={'class':'form-control','id' :'packageName'}),
#            'packageDuration':forms.NumberInput(attrs={'class':'form-control'}),
#            'price':forms.NumberInput(attrs={'class':'form-control'}),
#            'description':forms.Textarea(attrs={'class':'form-control'}),
#         #    'featured_img':forms.FileInput(attrs={'class':'form-control'}),
#            'isUnderRated':forms.CheckboxInput(attrs={'class':'form-control'})
          
#          }
        

