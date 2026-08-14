from django.urls import path, include
from .views import userCreate, APIUser
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView

router = DefaultRouter()
router.register("api-user",APIUser, basename="api-user")



urlpatterns = [
    path("create/",userCreate),
    path("",include(router.urls)),
    path("api/register/", RegisterView.as_view(), name="register"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
