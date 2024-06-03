from django.shortcuts import render
from .forms import SyudentRegistration
# Create your views here.

def formdata(request):
    if request.method=='POST':
        form = SyudentRegistration(request.POST)
        if form.is_valid():
            form.save()
            form = SyudentRegistration()
    else:
        form = SyudentRegistration()
    return render(request,'app/registration.html',{'form':form})