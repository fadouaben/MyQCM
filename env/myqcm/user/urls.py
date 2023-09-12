from django.urls import path
from . import views
from .views import RegisterView,LoginView

urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.connexion,name='login'),
    path('logout',views.deconnection,name='logout'),
    path('acceuil',views.acceuil,name='acceuil'),


    path('signup/',RegisterView.as_view(),name='signup'),
    path('signin/',LoginView.as_view(),name='signin'),
    
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),


]