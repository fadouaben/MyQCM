from django import forms
from .models import UserClass
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    
class Inscription(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
            
        ]

class InscriptionUser(forms.ModelForm) :
    class Meta():
        model = UserClass
        fields =[
            'tele',
            'role',
        ]      