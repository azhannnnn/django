from django.urls import path,include
from .views import home,regeister

urlpatterns = [
    path('',home,name='home'),
    path('register/',regeister,name='regeister')
   
]