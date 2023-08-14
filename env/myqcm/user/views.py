from django.shortcuts import render

from user.models import UserClass

# Create your views here.

def index(request):
    # ------------LoginForm3---------------

    if request.method == 'POST':
        dataForm = UserClass(request.POST)
        if dataForm.is_valid():
            dataForm.save()
    return render(request,'pages/index.html',{'lf':UserClass})
