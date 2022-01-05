from django.contrib import admin

from sales.models import ItemSale, Sale

# Register your models here.
class SaleItemInline(admin.TabularInline):
    model = ItemSale

class SaleAdmin(admin.ModelAdmin):
    inlines = (SaleItemInline,)
    list_display = (
        'date',
        'seller',
        'customer',
        'created',
        'modified',
    )
    
    readonly_fields=('created', 'modified',)
    list_filter=('created', 'modified')
    search_fields = ['created']
    
    @admin.display(empty_value='???')
    def date(self, obj):
        return obj.created.strftime('%d-%m-%Y')
    

admin.site.register(Sale,SaleAdmin)