from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets

from . import serializers, models

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
