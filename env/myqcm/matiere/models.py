from django.db import models
from niveau.models import Niveau

class Matiere(models.Model):
    titre = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    niveau  = models.ForeignKey(Niveau,on_delete=models.CASCADE)


# Create your models here.
