from django.shortcuts import render

# Create your views here.

#View for Register Page

def RegisterPage(request):
    return render(request,"register.html")

# View for user registration
def UserRegister(request):
    data = render(request,'register.html')
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']

    data.set_cookie('Fname',fname)
    data.set_cookie('Lname',lname)
    data.set_cookie('Email',email)
    data.set_cookie('Contact',contact)
    data.set_cookie('Password',password)
    
    return data

def getData(request):
    fname=request.COOKIES['Fname']
    lname=request.COOKIES['Lname']
    email=request.COOKIES['Email']
    contact=request.COOKIES['Contact']
    password=request.COOKIES['Password']


    data = {
        'FirstName':fname,
        'LastName':lname,
        'Email':email,
        'Contact' : contact,
        'Password' : password
    }
    
    return render(request,'home.html',data)


#Login VIew

def LoginPage(request):
    return render(request,"login.html")


# Login User
def LoginUser(request):
     return
