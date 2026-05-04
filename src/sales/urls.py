from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from sales.views import (
    ProductListView, 
    ProductCreateView,
    ProductUpdateView,
    SalesCreateView,
    SalesDetailView
)



urlpatterns = [

    path("products/", ProductListView.as_view(), name="product_list"),
    path("products/create/", ProductCreateView.as_view(), name="product_create"),
    path("products/update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),

    path("sales/create/", SalesCreateView.as_view(), name="sales_create"),
    path("sales/<int:pk>/", SalesDetailView.as_view(), name="sales_detail"),

    path("", RedirectView.as_view(pattern_name="product_list", permanent=False)),
]