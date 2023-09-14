from django.db import models
#from user.models import UserClass
#from matiere.models import MatiereClass


# Create your models here.
class Chapitre(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.CharField(max_length=100,null=True,blank=True)
    teacher = models.ForeignKey(to='user.UserClass',on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'role':'TEACHER'},related_name='chapitre_creé')
    student = models.ManyToManyField(to='user.UserClass',related_name='chapitres_suivis', blank=True,limit_choices_to={'role':'STUDENT'})
    matieree= models.ForeignKey(to='matiere.Matiere',on_delete=models.CASCADE,null=True,blank=True,related_name='matiere')
class Score(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(to='user.UserClass', on_delete=models.CASCADE)
    score = models.IntegerField()





    

      


