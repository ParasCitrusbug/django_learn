from django.urls import path
from student import views

urlpatterns = [
    path("student_list/", views.StudentDataList.as_view(), name="student_list"),
]
