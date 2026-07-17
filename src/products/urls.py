from django.urls import path

from .views import list_product, create_product, ProductAPIView

urlpatterns = [
    path("list", list_product),
    path("create",create_product),
    path("api/v1",ProductAPIView.as_view()),
]
