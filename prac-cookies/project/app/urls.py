from django.urls import path
from .views import *

urlpatterns = [
    path("",RegisterPage,name="registerpage"),
    path("getdata/",getData,name="getData"),
    path("register/",UserRegister,name="register"),
    path("loginpage/",LoginPage,name="loginpage"),
    path("loginuser/",LoginUser,name="login"),
]