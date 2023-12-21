from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import MessageModel


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageModel
        fields = '__all__'
