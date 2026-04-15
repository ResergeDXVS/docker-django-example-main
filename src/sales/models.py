from django.db import models

class Sales(models.Model):
    id              = models.IntegerField(primary_key=True,null=False,blank=False)
    

class Product(models.Model):
    id              = models.IntegerField(primary_key=True,null=False,blank=False)
    product_name    = models.CharField(max_length=50, null=False, blank=False)
    price           = models.FloatField(null=False, blank=False)