from django.urls import path,include
from .views import register,home
urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register')
]