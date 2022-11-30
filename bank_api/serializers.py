from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'cpf', 'email', 'wage', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['cpf', 'password', 'token']
        read_only_fields = ['token']