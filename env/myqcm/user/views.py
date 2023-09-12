from django.shortcuts import render,redirect

from .models import UserClass
from .form import Inscription,InscriptionUser

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from rest_framework.permissions import AllowAny


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from .serializers import UserClassSerializer
from django.middleware.csrf import get_token
from django.http import JsonResponse

# Create your views here.

# --------------Restframework------------

class RegisterView(APIView):
    def post(self,request):
        serializer = UserClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    permission_classes = [AllowAny] 
    
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = UserClass.objects.filter(user__username=username).first()

        if user is None:
            raise AuthenticationFailed('User not found')
        if not user.user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')
        decoded_token = jwt.decode(token,'secret',algorithms=['HS256'])
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data = {
            'jwt':token
        }
        return response
    

def get_csrf_token(request):
    csrf_token = get_token(request)
    response = JsonResponse({'csrfToken': csrf_token})
    return response



def index(request):
    # ------------LoginForm3---------------

    if request.method == 'POST':
        dataForm = Inscription(request.POST)
        if dataForm.is_valid():
            dataForm.save()
    return render(request,'index.html',{'lf':Inscription})

def acceuil(request):
    return render(request,'accueil.html')

def register(request):
    registered = False
    if request.method == 'POST':
        prd_form = Inscription(data=request.POST)
        form = InscriptionUser(data=request.POST)
        if form.is_valid() and prd_form.is_valid() :
            prd_user = prd_form.save()
            prd_user.save()
            user = form.save(commit=False)
            user.user = prd_user
            user.save()
            registered = True
            messages.success(request,'Votre compte a été bien créer')
            return HttpResponseRedirect('login')
        else:
            messages.error(request,"erreur")
            print(prd_form.errors,form.errors)
    else:    
        prd_form = Inscription()
        form = InscriptionUser()    
    content = {
        'registered':registered,
        'form1':prd_form,
        'form2':form
    }
    return render(request,'register.html', content)


def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.success(request,'bienvenu')
            return redirect('acceuil')  
        else:
            messages.error(request,"erreur d'authentification")
              


    return render(request,'login.html')


@login_required
def deconnection(request):
    logout(request)