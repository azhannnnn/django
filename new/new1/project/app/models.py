from django.db import models

class Student(models.Model):
    Fname = models.CharField(max_length=100,verbose_name='FNAME')
    Lname = models.CharField(max_length=100)
    Qualification = models.CharField(max_length=100)
    DOB = models.DateField()
    Language = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)

