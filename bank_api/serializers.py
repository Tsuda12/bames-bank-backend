from rest_framework import serializers
from .models import *
from random import randint
import decimal


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)
    agency = serializers.CharField(default='2582-0')
    # Random number generate
    number = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'cpf', 'email', 'wage', 'password', 'number', 'agency', 'balance']

    def get_number(self, obj):
        if obj.agency == "2582-0":
            number_account = ""
            for i in range(1, 8):
                rand_number = str(randint(1, 9))
                number_account += rand_number
            number_account_format = number_account+"-"+"0"
            return number_account_format

    def get_balance(self, obj):
        if obj.wage >= 0:
            balance_value = decimal.Decimal(randint(1000, 5000))
        return balance_value
    

    def create(self, validated_data):
        user = User.objects.create_superuser(
            username=validated_data['username'],
            cpf=validated_data['cpf'],
            email=validated_data['email'],
            wage=validated_data['wage'],
            password=validated_data['password'],
            agency=validated_data['agency'],
        )

        return user
        

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['cpf', 'password', 'token']
        read_only_fields = ['token']