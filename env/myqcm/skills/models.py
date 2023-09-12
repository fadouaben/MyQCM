from django.db import models

# Create your models here.

class Skill(models.Model):
    valeur = models.TextField()
    niveau = models.IntegerField(default=6)
    matiere = models.TextField(default='رياضبات')

    def __str__(self):
        return self.valeur
class SousSkill(models.Model):
    valeur = models.TextField()
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)

    def __str__(self) :
        return self.valeur