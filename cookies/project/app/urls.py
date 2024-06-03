from django.urls import path
from .views import home,getdata,delete

urlpatterns = [
    path('',home,name='home'),
    path('getdata/', getdata,name='getdata'),
    path('delete/',delete,name='delete'),
]
