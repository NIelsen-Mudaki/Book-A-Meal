from django.shortcuts import render
from customer.models import Customer
from orders.models import Orders
import datetime as dt

# Create your views here.
def orders(request):
    customer = request.user.id
    orders = Orders.get_orders_by_customer(customer)
    
    print(orders)
    return render(request,'orders.html',{'orders' : orders})

def order_history(request):
    orders = Orders.get_all_orders()
    error = ''
    if request.method == 'POST':
        search_date = request.POST['order_date']
        orders = Orders.objects.filter(order_date__icontains=search_date)
        if orders.exists():
            orders = Orders.objects.filter(order_date__icontains=search_date)
            error = ''
        else: 
            orders = Orders.get_all_orders()
            error = 'No orders for that date.'

    context = {
        'orders' : orders,
        'error': error,
    }
    return render(request, 'order-history.html',context)

# def search_results(request):
#     if 'order_date' in request.GET and request.GET['order_date']:
#         search_term = request.GET.get('order_date')
#         searched_orders = Orders.search_by_date(search_term)
#         message = f"{search_term}"
#         return render(request, 'order-history.html', {"message": message, "order_date":searched_orders})

#     else:
#         message = "You have not input any term"
#         return render(request, 'order-history.html', {"message": message})