from django.shortcuts import render
from datetime import datetime
from products.models import Product
from products.forms import ProductModelForm
# Create your views here.
def list_product(request):
    data = Product.objects.all()
    info = []
    for rec in data:
        info.append({
            "title":rec.title,
            "price":rec.price,
            "is_digital":rec.is_digital,
            "id":rec.id,
        })
    context = {
        "list_prod":info,
        "consult_time":datetime.now().today()
    }
    template = "products/product_list.html"
    return render(request,template,context)

def create_product(request):
    template ="products/product_create.html"
    form = ProductModelForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,template,{"form":form})