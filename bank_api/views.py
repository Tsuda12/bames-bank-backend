from rest_framework.generics import GenericAPIView
from rest_framework import response, status
from django.contrib.auth import authenticate
from rest_framework import permissions
from .serializers import *


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        
        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    serializer_class = UserSerializer
    authentication_classes = []

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    serializer_class = LoginSerializer
    authentication_classes = []

    def post(self, request):
        cpf = request.data.get('cpf', None)
        password = request.data.get('password', None)

        user = authenticate(username=cpf, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TransferAPIView(GenericAPIView):
    # queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    authentication_classes = []

    def post(self, request):
        send = User.objects.get(pk=request.data['send'])
        receive = User.objects.get(pk=request.data['receive'])
        value = decimal.Decimal(request.data['value'])

        print(send.password)

        if send.balance >= value:
            sender_object = {
                'username': send.username,
                'cpf': send.cpf,
                'email': send.email,
                'wage': send.wage,
                'agency': send.agency,
                'balance': send.balance - value,
                'password': send.password
            }
            serializer = UserSerializer(send, data=sender_object)

            if serializer.is_valid():
                serializer.save()
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            receive_object = {
                'username': send.username,
                'cpf': send.cpf,
                'email': send.email,
                'wage': send.wage,
                'agency': send.agency,
                'balance': send.balance + value,
                'password': send.password
            }
            serializer = UserSerializer(receive, data=receive_object)

            if serializer.is_valid():
                serializer.save()
            else:
                return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return 