from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model

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