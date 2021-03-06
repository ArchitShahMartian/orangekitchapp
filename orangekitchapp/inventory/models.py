from django.db import models


PRODUCT_CHOICES = [
    ('Plate Racks', 'Plate Racks'),
    ('Horizontal Plate Racks(Single)', 'Horizontal Plate Racks(Single)'),
    ('Horizontal Plate Racks(Double)', 'Horizontal Plate Racks(Double)'),
    ('Quarter Plate Racks(Double)', 'Quarter Plate Racks(Double)'),
    ('Quarter Plate Racks(Four Section)', 'Quarter Plate Racks(Four Section)'),
    ('Soup Bowl(Horizontal)', 'Soup Bowl(Horizontal)'),
    ('Soup Bowl(Vertical)', 'Soup Bowl(Vertical)'),
    ('Soup Bowl Racks (W/ Plate)', 'Soup Bowl Racks (W/ Plate)'),
    ('Katori Racks', 'Katori Racks'),
    ('Plizner Glass Racks', 'Plizner Glass Racks'),
    ('Wine Glass Racks', 'Wine Glass Racks'),
    ('Coffee Mug/Kulud Racks', 'COffee Mug/Kulud Racks'),
    ('Onion Potato Trolley', 'Onion Potato Trolley'),
    ('Onion Potato Trolley (W/ Partition)', 'Onion Potato Trolley (W/ Partition)'),
    ('Wine Holder', 'Wine Holder')
]

MATERIAL_CHOICES = [
    ('SS 202', 'SS 202'),
    ('SS 304', 'SS 304'),
    ('MS + PVC', 'MS +PVC'),
    ('SS + PVC', 'SS +PVC')
]

SIZE_CHOICES = [
    ('7.5 inch', '7.5 inch'),
    ('8 inch', '8 inch'),
    ('9 inch', '9 inch'),
    ('10 inch', '10 inch'),
    ('11 inch', '11 inch'),
    ('12 inch', '12 inch'),
    ('13 inch', '13 inch'),
    ('14 inch', '14 inch'),
    ('24 x 24 x 30', '24 x 24 x 30')
]

PRIORITY_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

WIRE_CHOICES = [
    (3, '3'),
    (5, '5'),
    (6, '6')
]


# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,
                                    choices=PRODUCT_CHOICES)
    # category = models.CharField(max_length=30) # No need of this field right now
    size = models.CharField(max_length=30,
                            choices=SIZE_CHOICES,
                            null=True,
                            blank=True)
    price = models.FloatField()
    weight = models.FloatField(null=True,
                               blank=True)
    material = models.CharField(max_length=30,
                                choices=MATERIAL_CHOICES)
    last_updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200,
                                   null=True,
                                   blank=True)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('product_name', 'size', 'material')

    def __str__(self):
        return '{} ({})'.format(self.product_name, self.size)


class WireSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    diameter = models.FloatField(choices=WIRE_CHOICES)
    length = models.FloatField()

    # def __str__(self):
    #     return '{} {} {}'.format(self.product, self.diameter, self.length)


class Customer(models.Model):
    company_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    primary_address = models.CharField(max_length=300)
    secondary_address = models.CharField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField()
    priority = models.CharField(max_length=1,
                                choices=PRIORITY_CHOICES)
    advance = models.IntegerField()


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

