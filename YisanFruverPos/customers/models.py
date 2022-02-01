from django.db import models

# Create your models here.
class Customer(models.Model):
    name= models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    document_number= models.CharField(max_length=20, blank=False, null=False, unique=True)
    email= models.EmailField(blank=False, null=False)
    address = models.CharField(max_length=50,blank=False, null=False)
    phone_number= models.CharField(max_length=20, blank=False, null=False)
    
    
    created= models.DateTimeField(auto_now_add=True)
    modified= models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Customers'
        verbose_name = ' Customer'