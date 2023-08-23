from django.shortcuts import render

from user.models import UserClass
from .form import Inscription
# Create your views here.

def index(request):
    # ------------LoginForm3---------------

    if request.method == 'POST':
        dataForm = Inscription(request.POST)
        if dataForm.is_valid():
            dataForm.save()
    return render(request,'index.html',{'lf':Inscription})
