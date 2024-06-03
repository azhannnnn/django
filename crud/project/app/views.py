from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def home(request):
    return render(request,'home.html')

def insert(request):
     Fname = request.POST.get('Fname')
     Lname = request.POST.get('Lname')
     Email = request.POST.get('Email')
     Contact = request.POST.get('Contact')
     
     Student.objects.create(
          Fname = Fname,
          Lname = Lname,
          Email = Email,
          Contact = Contact
     )
    
     return render(request,'home.html')

def show(request):
     
     user= Student.objects.all()
     
     return render(request,'show.html',{'data':user})


def deletepage(request,pk):
     data = Student.objects.get(id=pk)
     data.delete()
     user= Student.objects.all()
     # return redirect('show')
     return render(request,'show.html',{'data':user})

def editpage(request,pk):
     data = Student.objects.get(id=pk)
     return render(request,'edit.html',{'key':data})


def update(request,pk):
     data = Student.objects.get(id=pk)
     data.Fname = request.POST['Fname']
     data.Lname = request.POST['Lname']
     data.Email = request.POST['Email']
     data.Contact = request.POST['Contact']
     data.save()
     
     return render(request,'edit.html',{'key':data})