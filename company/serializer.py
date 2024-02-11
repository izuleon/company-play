from rest_framework import serializers

from company.models import IndustryChoices


def company_industry_validator(value):
    if value not in IndustryChoices:
        raise serializers.ValidationError(
            f"Invalid industry choice, try use {[names[0] for names in IndustryChoices.choices]}"
        )
    return value


class CompanyCreationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    industry = serializers.CharField(
        max_length=100, validators=[company_industry_validator]
    )
