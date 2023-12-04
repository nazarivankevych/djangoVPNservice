from rest_framework import serializers
from .models import UserProfile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'  # Include all fields or specify the fields you want to include
