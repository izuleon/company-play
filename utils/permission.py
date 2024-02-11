from rest_framework.permissions import BasePermission

from user.models import UserTypeChoices


class IsOwner(BasePermission):
    """
    Custom permission to check specific conditions for users.
    """

    def has_permission(self, request, view):
        """
        Checks if the user has necessary permissions.

        Args:
            request (rest_framework.request.Request): The request object.
            view (django.views.APIView): The view object.

        Returns:
            bool: True if the user has permission, False otherwise.
        """

        # Implement your custom logic here, e.g.:
        user = request.user
        if user.is_authenticated and user.user_type == UserTypeChoices.OWNER:
            return True
        return False  # Deny permission by default

    def has_object_permission(self, request, view, obj):
        """
        Optional method for object-level permission checks.

        Args:
            request (rest_framework.request.Request): The request object.
            view (django.views.APIView): The view object.
            obj (Model): The object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """

        # Implement your object-level logic here if needed

        return super().has_object_permission(request, view, obj)
