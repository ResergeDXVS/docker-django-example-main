from django.urls import path

from .views import list_product, create_product, ProductAPIView, ProductListView

urlpatterns = [
    path("list", list_product),
    path("create",create_product),
    path("api/v1",ProductAPIView.as_view()),
    path("products",ProductListView.as_view()),
]
