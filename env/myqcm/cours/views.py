from django.http import HttpResponse
from django.shortcuts import render
from cours.models import Cours
def afficher(request):
    cours = Cours.objects.all()
    return HttpResponse('<h1>Hello Django!</h1>{cours[0].titre}')
# Create your views here.
