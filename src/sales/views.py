from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DetailView
)
from .models import Product, SalesDetail, Sales
from .forms import ProductModelForm, SalesModelForm, SalesDetailModelForm




# Vista para la lista de productos
class ProductListView(ListView):
    model = Product
    template_name = "sales/productos.html"
    context_object_name = "products"
    
# Vista para crear productos
class ProductCreateView(CreateView):
    model=Product
    form_class = ProductModelForm
    template_name = "sales/productos_form.html"

# Vista para actualizar producto
class ProductUpdateView(UpdateView):
    model=Product
    form_class = ProductModelForm
    template_name = "sales/producto_detalle.html"

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs["pk"])
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    

#Vista para crear una venta
class SalesCreateView(CreateView):
    model = Sales
    form_class = SalesModelForm
    template_name = "sales/ventas_form.html"

    def form_valid(self, form):
        sale = form.save()
        return redirect("sales_detail", pk=sale.pk)
    
class SalesDetailView(DetailView):
    model = Sales
    template_name = "sales/ventas_detalle.html"
    context_object_name = "sale"
