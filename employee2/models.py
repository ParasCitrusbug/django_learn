from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class EmployeeData2(models.Model):
    employee_name = models.CharField(max_length=200)
    employee_id = models.CharField(max_length=200)
    employee_phone = models.CharField(max_length=10)
    employee_address = models.CharField(max_length=150)
    employee_working = models.BooleanField(default=True)
    employee_department = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.employee_name


CITY_CHOICES = (
    ("Rajkot", "Rajkot"),
    ("Ahmedabad", "Ahmedabad"),
    ("Amreli", "Amreli"),
    ("Baroda", "Baroda"),
)
class UserData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=25, null=False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False)
    city = models.CharField(max_length=25,choices=CITY_CHOICES,default="Rajkot")
