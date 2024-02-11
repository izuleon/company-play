from typing import Any

from django import forms

from user.models import User, UserTypeChoices


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput, required=False
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput, required=False
    )

    class Meta:
        model = User
        exclude = ["password"]

    def clean(self):
        cleaned_data = super().clean()
        instance = self.instance.pk
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if not instance:
            if not password1 or not password2:
                raise forms.ValidationError("Have to fill password on creations")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        company = cleaned_data.get("company")
        user_type = cleaned_data.get("user_type")
        if user_type == UserTypeChoices.EMPLOYEE:
            if company is None:
                raise forms.ValidationError("Employee cant have empty company")

        cleaned_data
