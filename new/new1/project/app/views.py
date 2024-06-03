from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .forms import Stu_form



def home(request):
     data = {}
     data['form']=Stu_form
     return render(request,'home.html',data)
def register(request):
     print(request.method)
     fname = request.POST['Fname']
     lname = request.POST['Lname']
     lang = request.POST['Language']
     quali = request.POST['Qualification']
     dob = request.POST['DOB']
     age = request.POST['Age']
     print(fname)
     print(lname)
     print(lang)
     print(quali)
     print(dob)
     print(age)
     # return render(request,'home.html')
