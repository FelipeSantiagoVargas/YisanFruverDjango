from django.contrib import admin
from providers.models import Provider

# Register your models here.
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name','category', 'phone_number','email','document_number')
    fieldsets = (('Provider', {
            'fields': (('name',), ('email',),('phone_number',), ('description',),('category',))
        }),
            ('Metadata', {
                'fields': (('created', 'modified'))
            }),
    )

    readonly_fields=('created', 'modified',)
    list_filter=('created', 'modified')
    search_fields = ['name']
    
admin.site.register(Provider,ProviderAdmin)