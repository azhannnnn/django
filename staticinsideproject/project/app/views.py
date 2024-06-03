from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.


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
    # return redirect("https://www.instagram.com/")

    student = [
        {
        'name' : 'John Doe',
        'age': 25,
        'city':'New York' },
        {
        'name' : 'Azhan khan',
        'age': 20,
        'city':'Bhopal' },
        {
        'name' : 'Adnan chodhry',
        'age': 20,
        'city':'New York' }
        
        ]
    return render(request,'home.html',{'data':student})