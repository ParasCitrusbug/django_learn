from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import EmployeeData2, UserData
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
import logging
from django.views import View
from employee2 import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Get an instance of a logger
logger = logging.getLogger(__name__)


class LoginUser(CreateView):
    """login user"""

    form_class = forms.UserForm
    template_name = "employees2/login.html"

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        fm = self.form_class(request.POST)
        user = UserData.objects.filter(email=email, password=password)
        if user and fm:
            request.session["email"] = "email"
            return redirect("home2")
        else:
            messages.error(request, "invalid email and password")
            return redirect("login")


class EmployeeHome(TemplateView):
    """view of employee data"""

    template_name = "employees2/home2.html"

    def get_context_data(self):

        employee_data = EmployeeData2.objects.all()
        context = {"employee_data": employee_data}
        return context


class AddEmployee(View):
    """Employee data add"""

    template_name = "employees2/add_employee2.html"
    employee_form = forms.EmployeeForm()

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        employee_name = request.POST.get("employee_name")
        employee_id = request.POST.get("employee_id")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        employee_working = request.POST.get("employee_working")
        employee_department = request.POST.get("employee_department")

        e = EmployeeData2()
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

        return redirect("home2")


class DeleteEmployee(View):
    """delete data of employee"""

    def get(self, request, id):
        emp_id = EmployeeData2.objects.get(pk=id)
        emp_id.delete()
        return redirect("home2")


class UpdateEmployee(View):
    """redicet to only update data of employee"""

    template_name = "employees2/update_employee2.html"

    def get(self, request, id):
        emp_id = EmployeeData2.objects.get(pk=id)
        context = {"emp": emp_id}
        return render(request, self.template_name, context)


class DoUpdateEmployee(View):
    """update date of employee"""

    def post(self, request, id):
        employee_name = request.POST.get("employee_name")
        employee_id = request.POST.get("employee_id")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        employee_working = request.POST.get("employee_working")
        employee_department = request.POST.get("employee_department")

        e = EmployeeData2.objects.get(pk=id)
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

        return redirect("home2")


class LogoutUser(View):
    def get(self, request):
        try:
            del request.session["email"]
        except KeyError:
            pass
        return HttpResponse("You're logged out.")
