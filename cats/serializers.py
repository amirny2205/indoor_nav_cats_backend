from rest_framework import serializers
from .models import CatModel


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatModel
        fields = '__all__'
