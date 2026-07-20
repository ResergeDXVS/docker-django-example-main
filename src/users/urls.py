from django.urls import path, include
from .views import userCreate, APIUser
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("api-user",APIUser, basename="api-user")



urlpatterns = [
    path("create/",userCreate),
    path("",include(router.urls)),
]
