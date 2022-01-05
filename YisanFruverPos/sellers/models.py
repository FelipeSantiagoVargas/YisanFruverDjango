from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Seller(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    document_number = models.CharField(max_length=20, blank=False, null=False, unique=True)
    phone_number = models.CharField(max_length=20, blank=False, null=False, unique=True)
    is_active = models.BooleanField(default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name_plural = 'Sellers'
        verbose_name = 'Seller'