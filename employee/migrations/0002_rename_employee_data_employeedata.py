# Generated by Django 4.1.7 on 2023-02-24 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employee_data',
            new_name='EmployeeData',
        ),
    ]