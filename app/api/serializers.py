from rest_framework import serializers
from .models import Plant, Category

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'
