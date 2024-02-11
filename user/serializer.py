# apps/your_app/serializers.py
from rest_framework import serializers

from company.models import IndustryChoices


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)


def company_industry_validator(value):
    if value not in IndustryChoices:
        raise serializers.ValidationError(
            f"Invalid industry choice, try use {[names[0] for names in IndustryChoices.choices]}"
        )
    return value


class OwnerSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    first_name = serializers.CharField(max_length=255, default=None)
    last_name = serializers.CharField(max_length=255, default=None)
    email = serializers.CharField(max_length=255, default=None)
    company_name = serializers.CharField(max_length=255)
    company_industry = serializers.CharField(
        max_length=100, validators=[company_industry_validator]
    )
