from django.contrib import admin
from django.db import models
from purchases.models import Purchase, ItemPurchase

# Register your models here.

class PurchaseItemInline(admin.TabularInline):
    model = ItemPurchase
    fieldsets = (
        (None, {
            "fields": (
                ('product','price_purchase','amount','earn','price_sale')
            ),
        }),
    )
    readonly_fields=('price_sale',)
    
    @admin.display(empty_value='???')
    def price_sale(self, obj):
        try:
            val = obj.price_purchase/obj.amount
            val = (val/(1-(obj.earn/100)))
            return val
        except :
            return 0

class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseItemInline,)
    list_display = (
        'date',
        'seller',
        'created',
        'modified',
    )
    
    readonly_fields=('created', 'modified',)
    list_filter=('created', 'modified')
    search_fields = ['created']
    
    @admin.display(empty_value='???')
    def date(self, obj):
        return obj.created.strftime('%d-%m-%Y')
    
    
    

admin.site.register(Purchase,PurchaseAdmin)
