from django.shortcuts import render
from customer.models import Customer
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.
def manageadmins_view(request):
    errors = ''
    success = ''
    try:
        users = Customer.objects.filter(is_Caterer=True).order_by('-id')[:5]
    except:
        users = 'nouser'
    if request.method == 'POST':
        fullnames = request.POST['fullnames']
        emailadress = request.POST['emailadress']
        phonenumber = request.POST['phonenumber']
        userpassword = request.POST['userpassword']
        
        finduser = Customer.objects.filter(email=emailadress)
        if finduser.exists():
            errors = 'sorry this user is already added'
        else:
            userpassword = make_password(userpassword)
            new_admin = Customer(customer_name=fullnames,email=emailadress,phone=phonenumber,password=userpassword, is_Caterer=True, is_Customer=False)
            new_admin.save()
            success = 'user successfully added.'
    context = {
        'title' : 'BOOK-A-MEAL | MANAGE - ADMINS',
        'errors':errors,
        'success':success,
        'users':users
    }
    return render(request, "manageadmins.html", context)



def editusers_view(request, id):
    return render(request, "edituser.html")