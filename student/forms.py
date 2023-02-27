from django import forms
from .models import Teacher,Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
