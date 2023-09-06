from django import forms
from .models import Chapitre, Score

class ChapitreForm(forms.ModelForm):
    class Meta:
        model = Chapitre
        fields = ['titre', 'teacher', 'student','joint_file']

class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ['chapitre', 'utilisateur', 'score']

