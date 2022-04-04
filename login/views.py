from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password,check_password
from customer.models import Customer

# Create your views here.
def login_view(request):
    errors = ''
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']
        checkpass = Customer.objects.filter(email = useremail)
        if checkpass.exists():
            getuser = Customer.objects.get(email = useremail)
            passwords = check_password(password, getuser.password)
            if passwords:
                response = redirect('/dashboard/')
                response.set_cookie("users",useremail)
                return response
            else:
                errors = 'Wrong password, please try again.'
        else:
            errors = 'sorry user with this email adress doesnt exist.'
    context = {
        'title':'BOOK-A-MEAL | LOGIN PAGE',
        'errors':errors
    }
    return render(request, "login.html", context)


def resetpass_view(request):
    success = ''
    errors= ''
    if request.method == 'POST':
        useremail = request.POST['useremails']
        password = request.POST['passwords']
        checkpass = Customer.objects.filter(email = useremail)
        if checkpass.exists():
            getuser = Customer.objects.get(email = useremail)
            getuser.password = make_password(password)
            getuser.save()
            success = 'password reset successfull.'
        else:
            errors = 'sorry user with this email dont exist.'
    context = {
        'title':'BOOK-A-MEAL | RESET-PASSWORDS',
        'success':success,
        'errors':errors
    }
    return render(request, "resetpass.html", context)

def delete_view(request, id):
    get_admin = Customer.objects.get(id =  id)
    get_admin.delete()
    return redirect("/manage-caterers/")


def logout_view(request):
    try:
        current_user = request.COOKIES['users']
    except:
        redirect("/")
    response = redirect("/")
    response.delete_cookie("users")
    return response