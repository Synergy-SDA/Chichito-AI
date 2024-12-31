from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.core.cache import cache
from .serializer import UserSerializer
from .services import Evaluation
from drf_spectacular.utils import extend_schema

class UserInformationAPIView(APIView):
    @extend_schema(
        request=UserSerializer,
        responses={
            200: UserSerializer,
            404: 'Not Found'
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            model = Evaluation(serializer)
            model.get_user_data()
            model.product_data()
            model.encoding()
            model.evaluate()
            return Response(1, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)