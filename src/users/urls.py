from django.urls import path
from .views import userCreate

urlpatterns = [
    path("create/",userCreate),
]
