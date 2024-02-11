# apps/your_app/views.py
import jwt
from django.contrib.auth import authenticate
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from company.models import Company
from test_case import settings
from user.models import User, UserTypeChoices
from user.serializer import OwnerSignUpSerializer, TokenSerializer


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


class OwnerSignUpView(APIView):
    @extend_schema(
        request=OwnerSignUpSerializer,
    )
    def post(self, request):
        serializer = OwnerSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        first_name = serializer.validated_data.get("first_name")
        last_name = serializer.validated_data.get("last_name")
        email = serializer.validated_data.get("email")
        company_name = serializer.validated_data.get("company_name")
        company_industry = serializer.validated_data.get("company_industry")

        new_user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        new_user.set_password(password)
        new_company = Company.objects.create(
            name=company_name,
            industry=company_industry,
            created_by=new_user,
        )
        new_user.company = new_company
        new_user.user_type = UserTypeChoices.OWNER
        new_user.save()
        return Response(
            {"message": f"User {new_user.get_full_name()} created"},
            status=status.HTTP_200_OK,
        )
