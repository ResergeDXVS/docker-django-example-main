from django.db import models
from django.urls import reverse

class Product(models.Model):
    product_name    = models.CharField(max_length=50, null=False, blank=False)
    price           = models.FloatField(null=False, blank=False)
    def __str__(self):
        return self.product_name
    
    def get_absolute_url(self):
        return reverse("product_list")
    

    def save(self,*args,**kwargs): 
        if self.price>0:
            super().save(*args,**kwargs)
        else:
            raise ValueError("Error en precio menor a 0")

class Sales(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Venta {self.id} - {self.date}"
    
    def get_absolute_url(self):
        return reverse("sales_detail",kwargs={"pk":self.pk})
    
class SalesDetail(models.Model):
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE, related_name="details")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity


