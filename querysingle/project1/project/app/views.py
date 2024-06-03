from django.shortcuts import render
from .models import Student

# def home(request):

#     # data = Student.objects.get(stu_city='pune')
#     # data = Student.objects.get(id='5').delete()
#     # data = Student.objects.first()
#     # data = Student.objects.last()
#     # data = Student.objects.earliest('id')
#     # data = Student.objects.latest('id')
#     data = Student.objects.order_by('stu_name').first()
#     # data = Student.objects.order_by('-stu_name').last()

#     name = data.stu_name
#     email = data.stu_email
#     contact = data.stu_contact
#     city = data.stu_city

#     user = {
#         'name':name,
#         'email':email,
#         'contact':contact,
#         'city':city
#     }
#     return render(request,'home.html',user)


def home(request):

    user = Student.objects.all()
    # user = Student.objects.values()
    # user = Student.objects.values_list()
    print(user)

    # for i in user:
        # print(i.id,i.stu_name,i.stu_email,i.stu_city,i.stu_contact)
    return render(request,'index.html',{'data':user})

    
