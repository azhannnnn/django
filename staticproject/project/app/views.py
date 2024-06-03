from django.shortcuts import render
from .models import User

def home(request):
    return render(request,'home.html')

def loginpage(request):
    return render(request,'login.html')

def login(request):
     if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.filter(email=email)
        if user:
            data = User.objects.get(email=email)
            if data.password == password:
                name = data.name
                email = data.email
                password = data.password
                user={
                    'name':name,
                    'email':email,
                    'password':password,
                }
                return render(request,"home.html",user)
            else:
                message = "Password does not match"
                return render(request,"login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"register.html",{'msg':message})
        

def registerpage(request):
    return render(request,'register.html')
def register(request):
    
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # First we will validate that user already exist
        user = User.objects.filter(email=email)

        if user: 
            message = "User already exist"
            return render(request,"register.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = User.objects.create(name=name,email=email,password=password)
                message = "User register Successfully"
                return render(request,"login.html",{'msg':message})
            else:
                message = "Password and Confirm Password Does not Match"
                return render(request,"register.html",{'msg':message}) 
            

