from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .forms import Student_form
from .models import Student

# def home(request):
#     return HttpResponse("kajshdfjgajslgflj")

# def home(request):
#     data={
#         "key" : "value",
#         "key1" : True,
#         "key2" : False,
#         "key3" : None,
    
#     }
#     return JsonResponse(data)

def home(request):

    data ={}
    data['form']=Student_form
    # return redirect("https://www.instagram.com/")
    # student = [
    #     {
    #     'name' : 'John Doe',
    #     'age': 25,
    #     'city':'New York' },
    #     {
    #     'name' : 'Azhan khan',
    #     'age': 20,
    #     'city':'Bhopal' },
    #     {
    #     'name' : 'Adnan chodhry',
    #     'age': 20,
    #     'city':'New York' }  
    #    ]
    # return render(request,'home.html',{'data':student})

    return render(request,'register.html',data)



def regeister(request):

    print(request.method)
    fname = request.POST['Fname']
    lname = request.POST['Lname']
    lang = request.POST['Language']
    quali = request.POST['Qualification']
    dob = request.POST['DOB']
    age = request.POST['Age']
    user = Student.objects.filter(Fname = fname)
    if user:
        msg = "Already registered"
     
    else:
     Student.objects.create(
           Fname = fname,
           Lname = lname,
           Qualification = quali,
           DOB = dob,
           Language = lang,
           Age = age,
           )
        
    return render(request,'home.html',{'data':msg}) 