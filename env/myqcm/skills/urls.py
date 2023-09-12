from rest_framework import routers
from django.urls import path, include
from .views import SkillViewSet,SousSkillViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'',SkillViewSet)
router.register(r'sous-skills',SousSkillViewSet)

urlpatterns = [
    path('skills/',include(router.urls)),
    path('',views.SkillListView.as_view(),name='skill-list'),
    path('<int:skill_id>/sous-skills/',views.SousSkillListView.as_view(),name='sousskill-list'),
]