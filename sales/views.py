from django.shortcuts import render

from orders.models import Orders

# Create your views here.

def sales(request):
    orders = Orders.get_all_orders()
    total_sales = Orders.get_grand_total()
    print(total_sales)
    print(orders)
    return render(request, 'sales.html', {'orders':orders, 'total_sales':total_sales})

