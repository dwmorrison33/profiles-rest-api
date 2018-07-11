from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets

from . import serializers, models

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""

        an_apiview= [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
