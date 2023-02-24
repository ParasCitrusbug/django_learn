from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=25)
    college = models.CharField(max_length=255)
    age = models.IntegerField(max_length=10)
    is_active = models.BooleanField(default=False)
