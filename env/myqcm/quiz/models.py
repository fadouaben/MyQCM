from django.db import models

# Create your models here.
class quiz(models.Model):
    question = models.TextField()
    response = models.TextField()
    choix = models.CharField()
    
