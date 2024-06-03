
from django.urls import path,include
# from . import views
# urlpatterns = [
#     path("",views.RegisterPage,name="registerpage"),
#     path("register/",views.UserRegister,name="register"),
#     path("loginpage/",views.LoginPage,name="loginpage"),
#     path("loginuser/",views.LoginUser,name="login"),
# ]

from .views import *
urlpatterns = [
    path("",RegisterPage,name="registerpage"),
    path("register/",UserRegister,name="register"),
    path("loginpage/",LoginPage,name="loginpage"),
    path("loginuser/",LoginUser,name="login"),
]