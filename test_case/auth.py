# apps/your_app/auth.py
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from user.models import User


class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            return None

        try:
            _, token_value = token.split()
            user = User.objects.get(token=token_value)
        except (ValueError, User.DoesNotExist):
            raise exceptions.AuthenticationFailed("Invalid token.")

        return user, None
