from django.db import models

class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.IntegerField()
    Course = models.CharField(max_length=50)
