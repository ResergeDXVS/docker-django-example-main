from django.shortcuts import render
from datetime import datetime
from products.models import Product
from products.forms import ProductModelForm

from rest_framework import views, generics
from rest_framework.response import Response

from .pagination import ProductCursorPagination
from .serializers import ProductSerializer

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


class ProductAPIView(views.APIView):
    def get(self, request):
        id_product = request.data.get("id")
        if not id_product:
            return Response({"message": "No se mandó ID."})
        
        product = Product.objects.filter(id=id_product).first()
        if not product:
            return Response({"message": "No se encontró ID %s" % id_product})
        
        data_product = {
            "title":product.title,
            "slug":product.slug,
            "description":product.description,
            "price":product.price,
            "is_digital":product.is_digital,
        }
        return Response(data_product)
            

    def post(self, request):
        required_fields = ["title", "price", "is_digital","description"]
        if not all(field in request.data for field in required_fields):
            return Response({"message": "No se mandó la información necesaria para registrar un producto."})

        product = Product.objects.create(
            title = request.data.get("title"),
            slug = request.data.get("title").replace(" ","-"),
            description = request.data.get("description"),
            price = request.data.get("price"),
            is_digital = bool(request.data.get("is_digital")),
        )

        return Response({"message": "Creado registro con ID %s" % product.id})

    def put(self, request):
        id_product = request.data.get("id")
        product = Product.objects.filter(id=id_product).first()
        if not product:
            return Response({"message": "No se encontró producto con ID %s" % id_product})

        required_fields = ["title", "price", "is_digital", "description"]
        if not all(field in request.data for field in required_fields):
            return Response({"message": "Faltan campos obligatorios para actualizar el producto."})

        # Actualizar todos los campos
        product.title = request.data.get("title")
        product.slug = request.data.get("title").replace(" ", "-")
        product.description = request.data.get("description")
        product.price = request.data.get("price")
        product.is_digital = bool(request.data.get("is_digital"))
        product.save()

        return Response({"message": "Producto %s actualizado con PUT" % product.id})
    
    def patch(self, request):
        id_product = request.data.get("id")
        product = Product.objects.filter(id=id_product).first()
        if not product:
            return Response({"message": "No se encontró producto con ID %s" % id_product})

        if "title" in request.data:
            product.title = request.data.get("title")
            product.slug = request.data.get("title").replace(" ", "-")
        if "description" in request.data:
            product.description = request.data.get("description")
        if "price" in request.data:
            product.price = request.data.get("price")
        if "is_digital" in request.data:
            product.is_digital = bool(request.data.get("is_digital"))

        product.save()

        return Response({"message": "Producto %s actualizado parcialmente con PATCH" % product.id})

    def delete(self, request):
        id_product = request.data.get("id")
        if not id_product:
            return Response({"message": "No se mandó ID."})
        product = Product.objects.filter(id=id_product).first()
        product.delete()
        return Response({"message": "Registro con ID %s eliminado" % id_product})
    
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductCursorPagination