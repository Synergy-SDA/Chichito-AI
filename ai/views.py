from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.cache import cache
from serializer import UserSerializer

class UserInformationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            # serializer.save()
            
        return Response(serializer.data ,status = status.HTTP_404_NOT_FOUND)
