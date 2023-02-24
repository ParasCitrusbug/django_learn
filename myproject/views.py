from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):

    if request.method == "POST":
        check = request.POST.get("name")
        print(check)

    date = datetime.datetime.now()
    is_active = True
    name = "paras pethani"
    student_data = {"Name": "milan", "email": "milan2gmail.com"}

    data = {
        "date": date,
        "is_active": is_active,
        "name": name,
        "student_data": student_data,
    }
    return render(request, "index.html", data)


def about(request):
    return HttpResponse("<h1>This is about page</h1>")


def service(request):
    return HttpResponse("<h1>This is service page</h1>")
