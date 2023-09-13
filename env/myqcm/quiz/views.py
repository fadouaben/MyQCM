from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
from .serializers import QuizSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from skills.models import SousSkill
# Create your views here.
api_key = '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'
openai.api_key = api_key

@api_view(['POST'])
def create_qcm(request):
    sous_skill = request.data.get('sous_skill_val')
    sous_skill_search = get_object_or_404(SousSkill, valeur=sous_skill)
    sous_skill_id = sous_skill_search.id

    prompt = f"Créez un QCM en arabe avec une seule question et les choix numérotés par les lettres arabes) sur le thème de '{sous_skill}'. Ne spécifiez pas la bonne réponse."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1000,
        
    )
    print(response.choices[0].text)
    qcm = response.choices[0].text
    prompt="sans introduction et sans inclure 'La lettre de la bonne réponse est :', donner la lettre arabe de bonne reponse de ce qcm : " + qcm
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
            
        )
    bonne_rep = response.choices[0].text
        

  

    quiz_data = {
        'question': qcm,
        'response': bonne_rep,
        'skill': sous_skill_id,
    }
    
    serializer = QuizSerializer(data=quiz_data)
    print('hi')
    if serializer.is_valid():
        serializer.save()
        print('hi')
        return Response({'qcm': qcm, 'response': bonne_rep}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    