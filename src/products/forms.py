from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "slug",
            "description",
            "price",
            "is_digital",
        ]
        exclude = [
            "image",
            "featured",
            "active",
            "tiemstamp",
        ]
        labels = {
            "title":"Agrega el nombre del producto",
            "slug":"Agrega el slug del producto",
            "description":"Añade la descripción del producto",
            "price":"Añade el precio del producto",
            "is_digital":"¿Es producto digital?",
        }

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title)<=10:
            raise forms.ValidationError("Debe de tener más de 10 caracteres")
        return title
    
    def clean_slug(self, *args, **kwargs):
        slug = self.cleaned_data.get("slug")
        if len(slug)<=10:
            raise forms.ValidationError("Debe de tener más de 10 caracteres")
        if " " in slug:
            raise forms.ValidationError("No debe de tener espacios")
        return slug
    
    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price<=0:
            raise forms.ValidationError("El precio debe ser mayor a 0.")
        return price