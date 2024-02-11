# apps/your_app/serializers.py
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)


class SignUpSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    first_name = serializers.CharField(max_length=255, default=None)
    last_name = serializers.CharField(max_length=255, default=None)
    email = serializers.CharField(max_length=255, default=None)
