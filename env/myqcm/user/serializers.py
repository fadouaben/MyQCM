from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import UserClass
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserClass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'email']

class UserClassSerializer(serializers.ModelSerializer):
    user = UserSerializer(write_only=True)  # Utilisez write_only pour éviter la sérialisation lors de la réponse

    class Meta:
        model = UserClass
        fields = [ 'user', 'tele', 'role']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)  # Créez un utilisateur avec les données de l'utilisateur

        user_class = UserClass.objects.create(user=user, **validated_data)  # Créez UserClass en utilisant l'utilisateur créé

        return user_class

