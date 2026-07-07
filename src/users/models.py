from django.db import models


GENDER = [
    ("female","Femenino"),
    ("male","Masculino"),
    ("other","Otro")
]

# Create your models here.
class User(models.Model):
    name            = models.CharField(max_length=100, blank=False, null=False)
    paternal_name   = models.CharField(max_length=100, blank=False, null=False)
    maternal_name   = models.CharField(max_length=100, blank=True, null=False)
    age             = models.IntegerField(blank=False, null=False)
    email           = models.EmailField(blank=False, null=False, unique=True)
    gender          = models.CharField(max_length=10, choices=GENDER, blank=False, null=False)
    phone           = models.CharField(max_length=20, blank=True, null=True)
    