from django.contrib import admin
from employee.models import EmployeeData, Testimonial

# Register your models here.
class emplopeeadmin(admin.ModelAdmin):
    list_display = ("employee_name", "employee_id")


admin.site.register(EmployeeData, emplopeeadmin)
admin.site.register(Testimonial)
