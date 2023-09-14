from django import forms
from .models import Niveau
class NiveauForm(forms.ModelForm):
    class Meta():
        model=Niveau
        fields = ('__all__')