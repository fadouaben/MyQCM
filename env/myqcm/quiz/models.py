from django.db import models
from skills.models import SousSkill

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    response = models.TextField()
    skill = models.ForeignKey(SousSkill,on_delete=models.CASCADE)