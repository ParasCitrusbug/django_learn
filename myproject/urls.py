"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from employee import urls
from django.conf import settings
from django.conf.urls.static import static
from student import urls
from employee2 import urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", index),
    path("about/", about),
    path("service/", service),
    path("employee/", include("employee.urls"), name="employee"),
    path("student/", include("student.urls"), name="student"),
    path("employee2/", include("employee2.urls"), name="employee2"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
