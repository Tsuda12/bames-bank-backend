from django.urls import path, include
from rest_framework_nested import routers
from .views import *

# router = routers.DefaultRouter()
# router.register('', TransferViewSet, basename='transfer')

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name='register'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('user', AuthUserAPIView.as_view(), name='user'),
    path('transfer', TransferAPIView.as_view(), name='transfer'),
]