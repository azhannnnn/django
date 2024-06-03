from django.shortcuts import render,redirect
from .models import User



def home(request):
    return render(request, 'home.html')

def insert(request):
    Name = request.POST['name']
    Email = request.POST['email']
    Contact = request.POST['contact']
    Course = request.POST['course']
    User.objects.create(Name=Name, Email=Email, Contact=Contact, Course=Course)
    return render(request,'home.html')


def show(request):
    users = User.objects.all()
    return render(request,'show.html',{'users':users})

def delete(request,pk):
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('show')

def edit(request,pk):
    user = User.objects.get(id=pk)
    return render(request,'edit.html',{'user':user})

def update(request,pk):
    Name = request.POST['Name']
    Email = request.POST['Email']
    Contact = request.POST['Contact']
    Course = request.POST['Course']
    user = User.objects.get(id=pk)
    user.Name = Name
    user.Email = Email
    user.Contact = Contact
    user.Course = Course
    user.save()
    return redirect('show')