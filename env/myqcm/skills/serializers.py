from rest_framework import serializers
from .models import Skill
from .models import SousSkill

class SousSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SousSkill
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    sous_skills = serializers.SerializerMethodField()
    class Meta:
        model = Skill
        fields = '__all__'

    def get_sous_skills(self,skill):
        sous_skills = SousSkill.objects.filter(skill=skill)
        sous_skill_serializer = SousSkillSerializer(sous_skills, many=True)
        return sous_skill_serializer.data    

