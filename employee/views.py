from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import EmployeeData


def employee_home(request):
    employee_data = EmployeeData.objects.all()
    return render(request, "employees/home.html", {"employee_data": employee_data})


def add_employee(request):
    if request.method == "POST":
        employee_name = request.POST.get("employee_name")
        employee_id = request.POST.get("employee_id")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        employee_working = request.POST.get("employee_working")
        employee_department = request.POST.get("employee_department")

        e = EmployeeData()
        e.employee_name = employee_name
        e.employee_id = employee_id
        e.employee_phone = employee_phone
        e.employee_address = employee_address
        e.employee_department = employee_department
        if employee_working is None:
            e.employee_working = False
        else:
            e.employee_working = True

        e.save()

    return render(request, "employees/add_employee.html")


def delete_employee(request, id):
    emp_id = EmployeeData.objects.get(pk=id)
    emp_id.delete()
    return redirect("/employee/home")

def update_employee(request, id):
    emp_id = EmployeeData.objects.get(pk=id)
    return render(request, "employees/update_employee.html", {"emp":emp_id})

def do_update_employee(request, id):
    if request.method=="POST":
        employee_name = request.POST.get("employee_name")
        employee_id = request.POST.get("employee_id")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        employee_working = request.POST.get("employee_working")
        employee_department = request.POST.get("employee_department")

        e = EmployeeData.objects.get(pk=id)
        e.employee_name = employee_name
        e.employee_id = employee_id
        e.employee_phone = employee_phone
        e.employee_address = employee_address
        e.employee_department = employee_department
        if employee_working is None:
            e.employee_working = False
        else:
            e.employee_working = True

        e.save()
        
    return redirect("/employee/home")