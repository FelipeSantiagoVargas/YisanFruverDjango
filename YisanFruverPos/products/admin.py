from django.contrib import admin
from products.models import Product
from products.models import ProductCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','earn_', 'category','modified')
    fieldsets = (('Product', {
            'fields': (('name', 'price', 'category'), ('description',))
        }),
            ('Metadata', {
                'fields': (('created', 'modified'))
            }),
    )

    readonly_fields=('created', 'modified',)
    list_filter=('created', 'modified')
    search_fields = ['name']
    
    @admin.display(empty_value='???')
    def earn_(self, obj):
        return '{}%'.format(obj.earn)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    fieldsets = (('Category', {
            'fields': (('name', 'description'))
        }),
            ('Metadata', {
                'fields': (('created', 'modified'))
            }),
    )

    readonly_fields=('created', 'modified',)
    list_filter=('name',)
    
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
