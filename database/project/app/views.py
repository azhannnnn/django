from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def home(request):
    return render(request,'home.html')

def login(request):
    print(request.method)
    fname=request.POST['fname']
    email=request.POST['email']

    print(fname)
    print(email)

    User.objects.create(
       name=fname,
       email=email 
    )
    return render(request,'login.html')
    # return HttpResponse('register')