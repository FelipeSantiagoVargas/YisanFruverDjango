from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login
from django.views.generic.detail import DetailView
from products.models import Product
from django.views.generic import TemplateView, ListView
from sales.models import ItemSale, Sale
import locale
from purchases.Purchase import Purchase
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

import serial
import traceback

# Create your views here.


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'sellers/profile.html'
    # queryset = Seller.objects.all()
    context_object_name = 'seller'

    def get_total_sale_today(self):
        sales = Sale.objects.all().filter(seller=self.request.user.id)
        # items = ItemSale.objects.all().filter(sale=sale.id)
        aux = 0
        for sale in sales:
            items = ItemSale.objects.all().filter(sale=sale.id)
            for item in items:
                aux = aux + (item.amount * item.price_sale)
        return aux

    def get_context_data(self, **kwargs):
        locale.setlocale(locale.LC_ALL,'')
        context = super().get_context_data(**kwargs)
        context["sales"] = locale.currency(self.get_total_sale_today(), grouping=True) 
        return context
    


class LoginView(LoginView):
    template_name = 'sellers/login.html'
    
class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'sellers/login.html'

class SellView(LoginRequiredMixin, ListView):
    template_name= 'sellers/sell.html'
    model = Product
    context_object_name = 'products'
    
@login_required
def add_product(request, product_id):
    try:
        ser = serial.Serial('/dev/ttyUSB1')
        value = ser.read(6)     # write a string
        value = float(value)
        ser.close()
    except:
        traceback.print_exc()
        ser = 0
    
    purchase = Purchase(request)
    product = Product.objects.get(id=product_id)
    try:
        value = int(request.POST['value'])
    except:
        value = 0
        
    if value != 0:
        purchase.add_product(product,value)
    else:
        purchase.add_product(product,ser)
    return redirect('sellers:sell')

@login_required
def delete_product(request, product_id):
    purchase = Purchase(request)
    product = Product.objects.get(id=product_id)
    purchase.delete(product)
    return redirect('sellers:sell')

@login_required
def save_purchase(request):
    purchase = Purchase(request)
    bill = purchase.confirm_save(request.user.id,1)
    try:
      value = int(request.POST['value'])
    except:
      value = bill['total']
    change = value-int(bill['total'])
    return render(request,'sellers/ticket.html',{'bill':bill,'value':value,'change':change})

# class Ticket(TemplateView):
#     template_name= 'sellers/ticket.html'