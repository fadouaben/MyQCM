from django.shortcuts import render
from chapitre.models import Chapitre
def afficher(request):
    chapitre = Chapitre.objects.all()
    return HttpResponse('<h1>Hello Django!</h1>')
# Create your views here.
