from django import forms
from .models import UserClass
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    
class Inscription(forms.ModelForm):
    class Meta:
        model = UserClass
        fields = '__all__'
        