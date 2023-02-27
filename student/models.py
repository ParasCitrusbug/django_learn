from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)



def __str__(self):
    return self.frist_name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    sur_name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_room = models.IntegerField()
    student_teacher = models.ManyToManyField(Teacher)


