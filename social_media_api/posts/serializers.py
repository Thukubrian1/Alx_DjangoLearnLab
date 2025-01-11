from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    # Using serializers.StringRelatedField for the author field
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    # Using serializers.StringRelatedField for the author field
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at', 'post']

class UserSerializer(serializers.Serializer):  # Using `serializers.Serializer` instead of `ModelSerializer`
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=254, required=False, allow_blank=True)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    def create(self, validated_data):
        # Manually handle user creation
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        user.password = make_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Handle updates for the User model
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance