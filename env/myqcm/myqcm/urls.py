"""
URL configuration for myqcm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from chapitre import views as chapitre_views

from cours import views as cours_views

urlpatterns = [
    path('admin/', admin.site.urls),
      path('chapitres/', chapitre_views.chapitre_list, name='chapitre_list'),
    path('chapitres/create/', chapitre_views.chapitre_create, name='chapitre_create'),
    path('chapitres/<int:pk>/', chapitre_views.chapitre_detail, name='chapitre_detail'),
    path('chapitres/<int:pk>/update/', chapitre_views.chapitre_update, name='chapitre_update'),
    path('chapitres/<int:pk>/delete/', chapitre_views.chapitre_delete, name='chapitre_delete'),
    
    path('cours/', cours_views.cours_list, name='cours_list'),
    path('cours/<int:pk>/', cours_views.cours_detail, name='cours_detail'),
    path('cours/create/', cours_views.cours_create, name='cours_create'),
    path('cours/update/<int:pk>/', cours_views.cours_update, name='cours_update'),
    path('cours/<int:pk>/delete/', cours_views.cours_delete, name='cours_delete'),
    
   
]
