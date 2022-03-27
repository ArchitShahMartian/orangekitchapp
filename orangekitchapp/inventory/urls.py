"""Define the urls for the sensors."""

from django.urls import path
from inventory.views import get_product_list

urlpatterns = [
    path('get-product-list/', get_product_list, name="get_product_list")
]
