from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path("registerpage/",registerpage,name="registerpage"),
    path("register/",register,name="register"),
    path("loginpage/",loginpage,name="loginpage"),
    path("login/",login,name="login"),


    path("about/",about,name="about"),
    path("contact/",contact,name="contact"),
    path("project/",project,name="project"),
    path("social/",social,name="social"),
    path("",logout,name="logout")
]