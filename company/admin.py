# Register your models here.
from django.contrib import admin

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


admin.site.register(Company, CompanyAdmin)
