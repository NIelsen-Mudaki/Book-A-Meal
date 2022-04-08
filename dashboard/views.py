from django.shortcuts import render
from customer.models import Customer
from orders.models import Order, Orders,OrderItem

# Create your views here.
def dashboard_view(request):
    admins = Customer.objects.filter(is_Caterer=True).count()
    clients = Customer.objects.filter(is_Customer=True).count()
    orders = OrderItem.objects.all().count()
    order_items=OrderItem.objects.all().order_by('-id')[:6]
    all_orders = []
    for items in order_items:
        totals = int(items.quantity) * int(items.menu_id.price)
        all_orders.append({"id":items.id,"totals":totals})
    #total sales
    order_item=OrderItem.objects.all()
    all_order = 0
    for items in order_item:
        totals_price = int(items.quantity) * int(items.menu_id.price)
        all_order = all_order +  totals_price
    context = {
        'title' : 'BOOK-A-MEAL | DASHBOARD',
        'admins':admins,
        'orders':orders,
        'clients':clients,
        'orderitems':order_items,
        'totals':all_orders,
        'sales':all_order
    }
    return render(request, "dashboard.html",context)