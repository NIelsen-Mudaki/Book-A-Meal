from django.shortcuts import render
from customer.models import Customer
from orders.models import Order, Orders,OrderItem
import datetime as dt

# Create your views here.
def orders(request):
    customer = request.user.id
    orders = Orders.get_all_orders()

    order_items=OrderItem.objects.all()
    all_orders = []
    for items in order_items:
        totals = int(items.quantity) * int(items.menu_id.price)
        all_orders.append({"id":items.id,"totals":totals})
    for item in order_items:

        # item['subtotal']=int(item.quantity * item.menu_id.price)
        print(item.order.order_ref)
    
    print(orders)
    context={
        'orders' : orders,
        'orderitems':order_items,
        'totals':all_orders
    }
    return render(request,'orders.html',context)

def order_history(request):
    orders = Orders.get_all_orders()
    order_items=OrderItem.objects.all()
    print(order_items)
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
        'orderitems':order_items

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