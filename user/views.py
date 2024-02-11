import jwt
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from test_case import settings
from user.models import User, UserTypeChoices
from user.serializer import SignUpSerializer, TokenSerializer
from utils.permission import IsOwner


class UserLoginView(APIView):
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
            tokens = RefreshToken.for_user(user)
            return Response(
                {"token": str(tokens.access_token)}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED
            )


class OwnerSignUpView(APIView):
    @extend_schema(
        request=SignUpSerializer,
    )
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        first_name = serializer.validated_data.get("first_name")
        last_name = serializer.validated_data.get("last_name")
        email = serializer.validated_data.get("email")

        new_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type=UserTypeChoices.OWNER,
        )
        new_user.set_password(password)
        new_user.save()
        return Response(
            {"message": f"User {new_user.get_full_name()} created"},
            status=status.HTTP_200_OK,
        )


class RegisterEmployeeView(APIView):
    permission_classes = [IsOwner]

    @extend_schema(
        request=SignUpSerializer,
    )
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        first_name = serializer.validated_data.get("first_name")
        last_name = serializer.validated_data.get("last_name")
        email = serializer.validated_data.get("email")

        new_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            user_type=UserTypeChoices.EMPLOYEE,
        )
        new_user.set_password(password)
        new_user.company = request.user.company
        new_user.save()
        return Response(
            {"message": f"User {new_user.get_full_name()} created"},
            status=status.HTTP_200_OK,
        )
