from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework import status,views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BankUser,UserPayMethod,UserTransaction
from .serializers import UserSerializer,PayMethodSerializer,TransacSerializer

@api_view(['GET', 'POST','DELETE'])
def get_user(request): 
    if request.method == 'GET':
        data = BankUser.objects.all()
        serializers = UserSerializer(data, many=True)
        return Response(serializers.data)

@api_view(['GET', 'POST','DELETE'])
def get_paymethod(request): 
    if request.method == 'GET':
        data = UserPayMethod.objects.all()
        serializers = PayMethodSerializer(data, many=True)
        return Response(serializers.data)

@api_view(['GET', 'POST','DELETE'])
def get_transc(request): 
    if request.method == 'GET':
        data = UserTransaction.objects.all()
        serializers = TransacSerializer(data, many=True)
        return Response(serializers.data)

