from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication

from . import serializers, models, permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
