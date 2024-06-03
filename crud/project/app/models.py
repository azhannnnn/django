from django.db import models

class Student(models.Model):
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact = models.IntegerField()
