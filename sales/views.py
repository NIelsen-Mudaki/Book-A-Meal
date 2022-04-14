from django.shortcuts import render

from orders.models import Orders,OrderItem

# Create your views here.

def sales(request):
    orders = Orders.get_all_orders()
    # total_sales = Orders.get_grand_total()
    order_items=OrderItem.objects.all()
    all_orders = []
    total_sales=0

    for items in order_items:
        totals = int(items.quantity) * int(items.menu_id.price)
        total_sales+=totals
        all_orders.append({"id":items.id,"totals":totals})
    print(total_sales)
    print(orders)
    context={
        'orders' : orders,
        'orderitems':order_items,
        'totals':all_orders,
        'orders':orders, 
        'total_sales':total_sales
    }
    return render(request, 'sales.html',context)

