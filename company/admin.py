# Register your models here.
from typing import Any

from django.contrib import admin
from django.http.request import HttpRequest

from company.models import Company


class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "created_by",
    ]
    readonly_fields = [
        "created_by",
        "updated_by",
    ]

    def get_readonly_fields(self, request, obj):
        if request.user.is_superuser:
            return []
        return super().get_readonly_fields(request, obj)


admin.site.register(Company, CompanyAdmin)
