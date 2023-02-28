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
        widgets ={
            "email" :forms.EmailInput( attrs={"class":"form-control"}),
            "password" :forms.TextInput(attrs={"class":"form-control"})
        }