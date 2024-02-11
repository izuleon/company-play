# Register your models here.
from typing import Any
from django.contrib import admin
from django.forms import ValidationError
from user.forms import CustomUserCreationForm

from user.models import User, UserTypeChoices


class UserAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "username",
        "email",
    ]
    readonly_fields = [
        "last_login",
        "password",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    
    form = CustomUserCreationForm
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        obj.set_password(form.cleaned_data.get("password1"))
        obj.save()

admin.site.register(User, UserAdmin)
