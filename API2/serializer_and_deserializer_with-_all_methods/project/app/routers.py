from django.urls import path,include
from rest_framework import routers
from . import views
from .serializers import MyFormSerializer

router = routers.DefaultRouter()
router.register(r"app", views.my_form_view, basename="app")

urlpatterns = [
    path("", include(router.urls)),
]