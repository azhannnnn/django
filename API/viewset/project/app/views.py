from django.shortcuts import render
from django.http import HttpResponse

from .models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .serializers import UserSerializer
from rest_framework import viewsets
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


# def home(request):
#     data = User.objects.all()
#     print(data)
#     data1 = UserSerializer(data,many=True)
#     print(data1.data)
#     json_data = JSONRenderer().render(data1.data)
#     return HttpResponse(json_data,content_type='application/json')