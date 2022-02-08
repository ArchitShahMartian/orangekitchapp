from django.db import models


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    price = models.FloatField()
    weight = models.FloatField()
    material = models.CharField(max_length=30)
    last_updated_at = models.DateTimeField(auto_now=True)
