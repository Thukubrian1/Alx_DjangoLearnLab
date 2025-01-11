from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Define fields explicitly using `serializers.CharField()`
    username = serializers.CharField(max_length=150, required=True)
    email = serializers.CharField(max_length=254, required=True)
    first_name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    last_name = serializers.CharField(max_length=150, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        read_only_fields = ['id']

    def create(self, validated_data):
        # Use `get_user_model().objects.create_user` to create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        # Generate a token for the user
        Token.objects.create(user=user)
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
    

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'following', 'followers']
        read_only_fields = ['id', 'username', 'followers']