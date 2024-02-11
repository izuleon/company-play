# urls.py
from django.urls import path

from .views import OwnerSignUpView, RegisterEmployeeView, UserLoginView

urlpatterns = [
    path("login/", UserLoginView.as_view()),
    path("signup/", OwnerSignUpView.as_view()),
    path("register-employee/", RegisterEmployeeView.as_view()),
]
