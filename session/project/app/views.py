from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
     
     request.session['name']="azhan"
     request.session['city']="Bhopal"
     request.session['roll']="118"

     return render(request,'home.html')

def get(request): 
     if 'name' in request.session:
       name = request.session["name"]
       city = request.session["city"]
       roll = request.session["roll"]
       request.session.modified =  True
       data = {
          'Name':name,
          'City':city,
          'Roll':roll}
       return render(request,"get.html",data)
     else:
         return HttpResponse("<h1>Session Expired!!!!!</h1>")

def delete(request):
     
     del request.session["name"]
     del request.session["city"]
     del request.session["roll"]
     request.session.flush()
     
     return render(request,'delete.html')
