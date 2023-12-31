from django.db import models


# Create your models here.
class RoleChoices(models.TextChoices):
    ADMIN = 'admin'
    STUDENT = 'student'
    TEACHER = 'teacher'


class UserClass(models.Model):
    username = models.CharField(max_length=50)
    firstName = models.CharField(max_length=50)
    SecondName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tele = models.IntegerField()
    role = models.CharField(max_length=20,choices=RoleChoices.choices,default=RoleChoices.STUDENT)
    password = models.CharField(max_length=12)


