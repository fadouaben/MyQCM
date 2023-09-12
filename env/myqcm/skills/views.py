from django.shortcuts import render
from rest_framework import viewsets
from .models import Skill,SousSkill
from .serializers import SkillSerializer,SousSkillSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SousSkillViewSet(viewsets.ModelViewSet):
    queryset = SousSkill.objects.all()
    serializer_class = SousSkillSerializer    

class SkillListView(APIView):
    def get(self,request):
        skills = Skill.objects.all()
        skill_serializer = SkillSerializer(skills,many=True)
        return Response(skill_serializer.data)
    
class SousSkillListView(APIView):
    def get(self,request,skill_id):
        sous_skills = SousSkill.objects.filter(skill__id=skill_id)
        sous_skill_serializer = SousSkillSerializer(sous_skills,many=True)
        return Response(sous_skill_serializer.data)
