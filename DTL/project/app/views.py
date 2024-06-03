from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    Name='Neeraj'
    Qualification='M.Tech'
    City='Bhopal'
    data={
        'nm':Name,
        'quali':Qualification,
        'ct':City,
        'dt':'''python is a high-level, general-purpose programming language. 
                its design philosophy emphasizes code readability with the use of 
                significant indentation''',
        'cap':'Welcome to login page'
    }
    return render(request,'home.html',data)
    