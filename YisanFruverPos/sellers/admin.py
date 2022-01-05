from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from sellers.models import Seller


# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'phone_number', 'document_number', 'is_active')
    fieldsets = (('Customer', {
            'fields': (('user'), ('document_number',),('phone_number',),('is_active',))
        }),
            ('Metadata', {
                'fields': (('created', 'modified'))
            }),
    )

    readonly_fields=('created', 'modified',)
    list_filter=('created', 'modified')
    search_fields = ['name']
    
    

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""
    model = Seller
    can_delete = False
    verbose_name_plural = 'Sellers'
    
class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )
    
admin.site.unregister(User)

admin.site.register(User,UserAdmin)
admin.site.register(Seller,SellerAdmin)
