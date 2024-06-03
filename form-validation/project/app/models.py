from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=100) # _ converted into space and first charector converted into Uppercase
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=20) # bydefalut required is True