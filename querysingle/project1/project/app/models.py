from django.db import models

class Student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.CharField(max_length=50)
    stu_contact = models.CharField(max_length=50)
    stu_city = models.CharField(max_length=50)
