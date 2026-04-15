from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from .models import Sales,Product

class SalesTemplateView(LoginRequiredMixin,TemplateView):
    template_name = "ventas.html"

    def dispatch(self, request, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return HttpResponse("No permitido", status=401)
        return super(SalesTemplateView,self).dispatch(request, *args, **kwargs)
    
    def get_context_data(self, *args, **kwargs):
        return super(SalesTemplateView,self).get_context_data(*args, **kwargs)
    

# Vista para la lista de productos
class ProductListView(ListView):
    model = Product
    template_name = "sales/productos.html"