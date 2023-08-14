from django.db import models

# Create your models here.
class Chapitre(models.Model):
    titre = models.CharField(max_length=100)


class Score(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
   #utilisateur = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    score = models.IntegerField()