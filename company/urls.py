# urls.py
from django.urls import path

from company.views import CompanyCreationView

urlpatterns = [
    path("create/", CompanyCreationView.as_view()),
]
