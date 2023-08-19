from django.db import models
from cours.models import Cours

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    response = models.TextField()
    choix = models.CharField(max_length=200)
    cours = models.ForeignKey(Cours,on_delete=models.CASCADE)