import logging
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .forms import StudentForm

# Create your views here.

# create logger
logger = logging.getLogger(__name__)

class StudentDataList(TemplateView):
    template_name = 'student/output.html'

    

