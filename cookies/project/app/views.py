from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     data = render(request,'home.html')
     data.set_cookie('name','Neeraj',max_age=24*60*60)
     data.set_cookie('city','Bhopal',max_age=15)

     return data

def getdata(request): 
     name = request.COOKIES["name"]
     city = request.COOKIES["city"]
     data = {
          'Name':name,
          'City':city
     }
     return render(request,"getdata.html",data)

def delete(request):
     data = render(request,'delete.html')
     data.delete_cookie('name')
     data.delete_cookie('city')

     return data