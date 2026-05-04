from django import forms
from .models import Product,Sales,SalesDetail

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "product_name",
            "price",
        ]
        
class SalesModelForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ["customer_name"]

class SalesDetailModelForm(forms.ModelForm):
    class Meta:
        model = SalesDetail
        fields = ["product", "quantity"]
        