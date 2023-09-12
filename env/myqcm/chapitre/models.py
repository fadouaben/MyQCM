from django.db import models
from matiere.models import Matiere


# Create your models here.
class Chapitre(models.Model):
    titre = models.CharField(max_length=100)
    matiere  = models.ForeignKey(Matiere,on_delete=models.CASCADE)




