from django.urls import path,include
from rest_framework import routers, serializers, viewsets
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('',home,name='home')
]