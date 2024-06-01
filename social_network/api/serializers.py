from django.contrib.auth.models import User
from .models import FriendRequest
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value.lower()

    def create(self, validated_data):
        email = validated_data['email'].lower()  # Ensure email is case-insensitive
        user = User(username=email, email=email)
        user.set_password(validated_data['password'])
        user.save()
        return user

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['id', 'from_user', 'to_user', 'status', 'created_at']
