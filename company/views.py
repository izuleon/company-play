# Create your views here.
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from company.models import Company
from company.serializer import CompanyCreationSerializer
from user.models import User, UserTypeChoices
from utils.permission import IsOwner


class CompanyCreationView(APIView):
    permission_classes = [IsOwner]

    @extend_schema(
        request=CompanyCreationSerializer,
    )
    def post(self, request):
        serializer = CompanyCreationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get("name")
        industry = serializer.validated_data.get("industry")

        new_company = Company.objects.create(
            name=name,
            industry=industry,
            created_by=request.user,
        )
        return Response(
            {"message": f"Company {new_company.name} created"},
            status=status.HTTP_200_OK,
        )
