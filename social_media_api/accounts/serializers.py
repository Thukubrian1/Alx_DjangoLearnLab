from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ['id', 'username', 'bio', 'profile_picture']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User()
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = User().objects.create_user(**validated_data)
        return user