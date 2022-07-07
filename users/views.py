from django.contrib.auth import login
from rest_framework import generics, views

from .serializers import SignUpSerializer, SignInSerializer


class SignUpView(generics.CreateAPIView):
    serializer_class = SignUpSerializer


class SingInView(generics.CreateAPIView):
    serializer_class = SignInSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)
