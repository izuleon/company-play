# apps/your_app/views.py
import jwt
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema
from test_case import settings
from user.serializer import TokenSerializer


class TokenObtainView(APIView):
    @extend_schema(
        request=TokenSerializer,
    )
    def post(self, request):
        serializer = TokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            tokens = jwt.encode(
                {"user_id": user.id}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response({"token": tokens}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
            )
