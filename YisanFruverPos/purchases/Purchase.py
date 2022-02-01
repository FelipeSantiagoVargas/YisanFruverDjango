from distutils.command.clean import clean
from itertools import product
from sales.models import ItemSale, Sale
from sellers.models import Seller
from customers.models import Customer
from products.models import Product
from purchases.context_processor import total_purchase

class Purchase:
    
    def __init__(self,request):
        self.request = request
        self.session = request.session
        purchase = self.session.get('purchase')
        
        if not purchase:
            self.session['purchase'] = {}
            self.purchase = self.session['purchase']
        else:
            self.purchase = purchase
            
    def add_product(self,product,amount):
        id = str(product.id)
        if id not in self.purchase.keys():
            self.purchase[id]={
                "product_id": product.id,
                "product_name": product.name,
                'price_original' : product.price,
                "price" : (product.price*amount),
                "amount" : amount,
            }
        else:
            self.purchase[id]["amount"] += amount
            self.purchase[id]["price"] += (product.price*amount)
            
        self.save_purchase()
        
    def save_purchase(self):
        self.session['purchase'] = self.purchase
        self.session.modified = True
        
    def delete(self,product):
        id = str(product.id)
        if id in self.purchase:
            print(self.purchase[id]) 
            del self.purchase[id]
            self.save_purchase()
            
    def clean(self):
        self.session['purchase'] = {}
        self.session.modified = True
        
    def confirm_save(self,seller_id,customer_id):
        seller = Seller.objects.get(id=seller_id)
        customer = Customer.objects.get(id=customer_id)
        sale = Sale.objects.create(seller=seller, customer=customer)
        for value in self.session['purchase'].items():
            product = Product.objects.get(id=value[1]['product_id'])
            item = ItemSale.objects.create(sale=sale,product=product,price_sale=value[1]['price_original'],amount=value[1]['amount'])
            item.save()
        
        aux = total_purchase(self.request)
        self.purchase['sale'] = sale
        self.purchase['customer'] = customer
        self.purchase['total'] = aux['total_purchase']
        bill = self.session['purchase']
        self.clean()
        return bill
        
        