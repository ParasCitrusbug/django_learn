from django.urls import path
from employee2 import views
from employee2.views import (
    EmployeeHome,
    AddEmployee,
    DeleteEmployee,
    UpdateEmployee,
    DoUpdateEmployee,
)

urlpatterns = [
    # path("home2/", views.employee_home2, name="home2"),
    path("home2/", EmployeeHome.as_view(), name="home2"),
    path("add_employee2/", AddEmployee.as_view(), name="add_employee2"),
    path(
        "delete_employee2/<int:id>", DeleteEmployee.as_view(), name="delete_employee2"
    ),
    path(
        "update_employee2/<int:id>", UpdateEmployee.as_view(), name="update_employee2"
    ),
    path(
        "do_update_employee2/<int:id>",
        DoUpdateEmployee.as_view(),
        name="do_update_employee2",
    ),
]
