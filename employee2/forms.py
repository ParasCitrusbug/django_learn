from django import forms
from employee2 import models


class EmployeeForm(forms.Form):
    """Employee data form"""

    class Meta:
        model = models.EmployeeData2
        fields = "__all__"


class UserForm(forms.ModelForm):
    """User data form"""

    class Meta:
        model = models.UserData
        fields = ("email", "password")
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.TextInput(attrs={"class": "form-control"}),
        }


class ForgotPasswordForm(forms.ModelForm):
    """fargot password"""

    class Meta:
        model = models.UserData
        fields = ["email"]
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }


class ChangePasswordForm(forms.Form):
    """Change password"""

    new_password = forms.CharField()
    comfirm_password = forms.CharField()

    new_password.widget.attrs = {"class": "form-control"}
    comfirm_password.widget.attrs = {"class": "form-control"}
