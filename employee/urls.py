from django.urls import path
from employee import views

urlpatterns = [
    path("home/", views.employee_home, name= "home"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("delete_employee/<int:id>", views.delete_employee, name="delete_employee"),
    path("update_employee/<int:id>", views.update_employee, name="update_employee"),
    path("do_update_employee/<int:id>", views.do_update_employee, name="do_update_employee"),

]
