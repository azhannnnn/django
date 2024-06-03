from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    form = AadharForm()
    form1 = AllotForm()
    return render(request,'home.html',{'form':form,'form1':form1})


def add(request):
    adhar = request.POST['Adhar']
    
    check = Adhar.objects.filter(Adhar=adhar)

    if check:
        msg = "Adhar number exist"
        form = AadharForm()
        form1 = AllotForm()
        return render(request,'home.html',{'form':form,'form1':form1,'msg':msg})
        
    else:
        Adhar.objects.create(Adhar=adhar)
        msg = "Adhar number created"
        form = AadharForm()
        form1 = AllotForm()
        return render(request,'home.html',{'form':form,'form1':form1,'msg':msg})
    
def allot(request):
    name = request.POST['Name']
    email = request.POST['Email']
    id = request.POST['Adhar']

    data = Adhar.objects.get(id=id)
    

    Allot.objects.create(Name=name,Email=email,Adhar=data)
    msg = "User Details saved successfully"
    form = AadharForm()
    form1 = AllotForm()
    return render(request,'home.html',{'form':form,'form1':form1,'msg2':msg})
    