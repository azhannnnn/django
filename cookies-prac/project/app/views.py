from django.shortcuts import render


def home(request):
    return render(request,'home.html')

def loginpage(request):
    return render(request,'login.html')

def login(request):
     if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = request.COOKIES['email'] == email
        passw = request.COOKIES['password'] == password
        name = request.COOKIES['name']
        if user:
            if passw:

                user={
                    'name':name,
                    'email':email,
                    'pass':password,
                }
                return render(request,"about.html",user)
            else:
                message = "Password does not match"
                return render(request,"login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"register.html",{'msg':message})
        

def registerpage(request):
    return render(request,'register.html')
def register(request):
    
    data = render(request,'login.html')
    
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']
    data.set_cookie('name',name)
    data.set_cookie('email',email)
    data.set_cookie('password',password)
    data.set_cookie('cpassword',cpassword)
    if password == cpassword:
        return data
    else:
        message = "Password and Confirm Password Does not Match"
        return render(request,"register.html",{'msg':message}) 
           
            

def about(request):
    email = request.COOKIES['email']
    passw = request.COOKIES['password']
    name = request.COOKIES['name']
    user={
            'name':name,
            'email':email,
            'pass':passw,
        }
    return render(request,'about.html',user)

def contact(request):
    return render(request,'contact.html')

def project(request):
    return render(request,'project.html')

def social(request):
    return render(request,'social.html')

def logout(request):
    return render(request,'home.html')