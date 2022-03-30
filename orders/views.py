from django.shortcuts import render
from customer.models import Customer
from orders.models import Orders

# Create your views here.
def orders(request):
    customer = request.user.id
    orders = Orders.get_orders_by_customer(customer)
    print(orders)
    return render(request,'orders.html',{'orders' : orders})