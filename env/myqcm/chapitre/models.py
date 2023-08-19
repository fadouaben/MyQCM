from django.db import models
from user.models import UserClass

# Create your models here.
class Chapitre(models.Model):
    titre = models.CharField(max_length=100)
    teacher = models.ForeignKey(UserClass,on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'role':'TEACHER'})
    student = models.ManyToManyField(UserClass,related_name='chapitres_suivis', blank=True,limit_choices_to={'role':'STUDENT'})

class Score(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(UserClass, on_delete=models.CASCADE)
    score = models.IntegerField()


