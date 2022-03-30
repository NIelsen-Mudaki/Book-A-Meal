from django.shortcuts import render

from orders.models import Orders

# Create your views here.
def sales(request):
    orders = Orders.get_all_orders()
    print(orders)
    return render(request, 'sales.html', {'orders':orders})