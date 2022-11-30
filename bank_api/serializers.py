from rest_framework import serializers
from models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'cpf', 'email', 'wage',]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)