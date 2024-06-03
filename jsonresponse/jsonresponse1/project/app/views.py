from django.shortcuts import render
from django.http import JsonResponse

def home(request):
  data={
    'azhan' : 2000
  }
  return JsonResponse(data)
