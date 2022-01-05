from django.db import models
from products.models import ProductCategory

# Create your models here.

class Provider(models.Model):
    
    name = models.CharField(max_length=40, unique=True,blank=False,null=False)
    email= models.EmailField(blank=False, null=False)
    phone_number= models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField(blank=True,null=True)
    document_number= models.CharField(max_length=20, blank=True, null=True, unique=True)
    category = models.ForeignKey('products.ProductCategory', on_delete=models.RESTRICT)
    
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Providers'
        verbose_name = 'Provider'
        # abstract = True