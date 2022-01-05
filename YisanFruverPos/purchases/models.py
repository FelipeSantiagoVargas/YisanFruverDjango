from django.db import models

from sellers.models import Seller
from products.models import Product

# Create your models here.

class Purchase(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through='ItemPurchase', through_fields=('purchase','product'))
    
    def __str__(self):
        return self.created.strftime('%d-%m-%Y')


class ItemPurchase(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price_purchase = models.IntegerField(blank=False,null=False)
    amount = models.SmallIntegerField(blank=False,null=False)
    earn = models.SmallIntegerField(default=30, blank=False,null=False)
    
    def __str__(self):
        return self.product.name
    
    class Meta:
        unique_together = [['purchase','product']]
    
