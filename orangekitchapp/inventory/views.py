from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from inventory.models import Product
from django.core import serializers


# Create your views here.
def get_product_list(request):
    product_list = Product.objects.all().values_list('product_name',
                                                     'size',
                                                     'price',
                                                     'quantity',
                                                     'material')
    return JsonResponse(dict([("data", list(product_list))]))

