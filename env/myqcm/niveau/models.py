from django.db import models
from user.models import UserClass


# Create your models here.
class Niveau(models.Model):
    niveau = models.CharField(max_length=100)
    teacher = models.ForeignKey(UserClass,on_delete=models.CASCADE,null=True,blank=True,limit_choices_to={'role':'TEACHER'})
    student = models.ManyToManyField(UserClass,related_name='chapitres_suivis', blank=True,limit_choices_to={'role':'STUDENT'})

# Create your models here.
