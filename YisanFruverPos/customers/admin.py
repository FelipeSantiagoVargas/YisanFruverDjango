from django.contrib import admin
from customers.models import Customer

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','last_name', 'document_number','email', 'phone_number','created')
    fieldsets = (('Customer', {
            'fields': (('name','last_name'), ('document_number',), ('email',),('phone_number',))
        }),
            ('Metadata', {
                'fields': (('created', 'modified'))
            }),
    )

    readonly_fields=('created', 'modified',)
    list_filter=('created', 'modified')
    search_fields = ['name']
    
admin.site.register(Customer,CustomerAdmin)