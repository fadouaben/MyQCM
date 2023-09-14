from django.db import models
#from chapitre.models import chapitreClass
# Create your models here.
class Niveau(models.Model):
    nom = models.CharField(max_length=100)
    matieres = models.ManyToManyField(to='matiere.Matiere',related_name='matieres_niveau', blank=True)
