#Django imports
from django.db import models
from django.urls import reverse


# This models is the reference to product in a Fruver
class Product(models.Model):
    name = models.CharField(max_length=40, unique=True,blank=False,null=False)
    price = models.IntegerField(blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    stock = models.SmallIntegerField(blank = True, null=True)
    category = models.ForeignKey('ProductCategory', on_delete=models.RESTRICT)
    earn = models.SmallIntegerField(blank = False, null=False, default=30)
    
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Book
        """
        return reverse('product-detail', args=[str(self.id)])
    
    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = ' Product'
    
 
#This models represents the category of a product.    
class ProductCategory(models.Model):
    name = models.CharField(max_length=40,unique=True,blank=False,null=False)
    description = models.TextField(blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories Products'
        verbose_name = 'Category Product'
    
