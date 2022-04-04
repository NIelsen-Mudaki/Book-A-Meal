from django.shortcuts import render
from customer.models import Customer
from orders.models import Orders

# Create your views here.
def dashboard_view(request):
    admins = Customer.objects.filter(is_Caterer=True).count()
    clients = Customer.objects.filter(is_Customer=True).count()
    orders = Orders.objects.all().count()
    try:
        items = Orders.objects.all().order_by('-id')[:5]
    except:
        items = 'noitem'
    context = {
        'title' : 'BOOK-A-MEAL | DASHBOARD',
        'admins':admins,
        'orders':orders,
        'clients':clients,
        'items':items
    }
    return render(request, "dashboard.html",context)