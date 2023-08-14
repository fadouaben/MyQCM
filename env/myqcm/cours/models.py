from django.db import models

# Create your models here.
class Cours(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()

