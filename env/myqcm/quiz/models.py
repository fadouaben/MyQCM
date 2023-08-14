from django.db import models

# Create your models here.
class Quiz(models.Model):
    question = models.TextField()
    response = models.TextField()
    choix = models.CharField(max_length=200)
