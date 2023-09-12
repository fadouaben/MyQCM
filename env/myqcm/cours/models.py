from django.db import models
from chapitre.models import Chapitre,Skill
# Create your models here.
class Cours(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    chapitre = models.ForeignKey(Chapitre,on_delete=models.CASCADE)


class SousSkill(models.Model):
    valeur = models.TextField()
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)
