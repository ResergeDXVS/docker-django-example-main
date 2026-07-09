from django.urls import path

from .views import list_product, create_product

urlpatterns = [
    path("list", list_product),
    path("create",create_product),
]
