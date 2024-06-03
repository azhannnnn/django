from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home , name='home'),
    path('insert/',views.insert,name='insert'),
    path('show/',views.show,name='show'),

    path('editpage/<int:pk>/',views.editpage,name='editpage'),
    path('deletepage/<int:pk>/',views.deletepage,name='deletepage'),
    path('update/<int:pk>/',views.update,name='update'),
]