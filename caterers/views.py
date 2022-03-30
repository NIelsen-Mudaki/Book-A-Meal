from django.shortcuts import render
from customer.models import Customer
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def manageadmins_view(request):
    context = {
        'title' : 'BOOK-A-MEAL | MANAGE - ADMINS'
    }
    return render(request, "manageadmins.html", context)