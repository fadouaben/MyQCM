from django.db import models
#from chapitre.models import chapitreClass


# Create your models here.
class Matiere(models.Model):
    nom = models.CharField(max_length=100,null=True,blank=True)
    chapitres = models.ManyToManyField(to='chapitre.Chapitre',related_name='chapitress', blank=True)
    niveau= models.ForeignKey(to='niveau.Niveau',on_delete=models.CASCADE,null=True,blank=True,related_name='niveau')