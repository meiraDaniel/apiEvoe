from django.shortcuts import render
from rest_framework import generics

from users.serializers import UserSerializer
from django.contrib.auth.models import User


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Create your views here.
