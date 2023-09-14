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
from matiere import views as matiere_views
from niveau import views as niveau_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('niveaux/', niveau_views.afficher_niveau, name="listeNiveaux"),
    path('matieres/', matiere_views.afficher_matiere, name="listeMatieres"),
    path('CreateMatiere/', matiere_views.MatierCreateView.as_view(),name="MatiereCreate"),
    path('matieres/edit/<int:matiere_id>/', matiere_views.edit_matiere, name='edit_matiere'),
    path('matieres/delete/<int:matiere_id>/', matiere_views.delete_matiere, name='delete_matiere'),
    path('CreateNiveau/', niveau_views.NiveauCreateView.as_view(),name="NiveauCreate"),
    path('niveaux/edit/<int:niveau_id>/', niveau_views.edit_niveau, name='edit_niveau'),
    path('niveaux/delete/<int:niveau_id>/', niveau_views.delete_niveau, name='delete_niveau'),
]    
