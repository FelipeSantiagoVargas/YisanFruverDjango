from django.db import models
from sellers.models import Seller
from customers.models import Customer
from products.models import Product
# Create your models here.
class Sale(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='ItemSale', through_fields=('sale','product'))
    
    def __str__(self):
        return self.created.strftime('%d-%m-%Y')


class ItemSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_sale = models.IntegerField(blank=False,null=False)
    amount = models.SmallIntegerField(blank=False,null=False)
    earn = models.SmallIntegerField(default=30, blank=False,null=False)
    
    def __str__(self):
        return self.product.name
    
    class Meta:
        unique_together = [['sale','product']]