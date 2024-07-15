from rest_framework import serializers
from .models import GenZUserProfile

class GenZUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenZUserProfile
        fields = '__all__'
