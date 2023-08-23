from django import forms
from .models import UserClass

    
class Inscription(forms.ModelForm):
    class Meta:
        model = UserClass
        fields = '__all__'
        