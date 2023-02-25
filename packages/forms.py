from django import forms
from .models import Packages



class Packageform(forms.ModelForm):
    class Meta:
        model=Packages
        fields = "__all__"

        # isUnderRated= forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    # def __init__(self, *args, **kwargs):
    #     super(Packageform, self).__init__(*args, **kwargs)
      
        
    #     for name, field in self.fields.items():
    #         field.widget.attrs.update({'class': 'form-control'})
            
    #     self.isUnderRated.widget.attrs.update({'class':'form-check-input'})    
       
        

