from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', home , name="home"),
    path('get/', get,name='get'),
    path('delete/',delete,name='delete'),
]