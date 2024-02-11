# urls.py
from django.urls import path

from .views import OwnerSignUpView, TokenObtainView

urlpatterns = [
    path("token/", TokenObtainView.as_view()),
    path("signup/", OwnerSignUpView.as_view()),
]
