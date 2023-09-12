from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class RoleChoices(models.TextChoices):
    ADMIN = 'admin'
    STUDENT = 'student'   
    TEACHER = 'teacher'


class UserClass(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    tele = models.IntegerField()
    role = models.CharField(max_length=20,choices=RoleChoices.choices,default=RoleChoices.STUDENT)
    def __str__(self):
        return self.user.username

