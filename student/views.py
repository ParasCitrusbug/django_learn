import logging
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .forms import StudentForm
from .models import *
import asyncio
from django.http import HttpResponse
from django.views import View
# Create your views here.

# create logger
logger = logging.getLogger(__name__)

class StudentDataList(ListView):
    model = Teacher
    template_name = "student/teacher_list.html"

    def get_queryset(self):
        return Teacher.objects.filter(first_name = "jay")
    
    def get_context_data(self, **kwargs):
        
        context =  super().get_context_data(**kwargs)
        context["name"] = Teacher.objects.all().order_by("first_name")
        return context
    
    def head(self, *args, **kwargs):
        
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Last-Modified': "last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')"},
        )
        return response
   


class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        # Perform io-blocking view logic using await, sleep for example.
        await asyncio.sleep(1)
        return HttpResponse("Hello async world!")
    

