from rest_framework import serializers
from .models import ARSession

class ARSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ARSession
        fields = '__all__'
