from django.shortcuts import render

# Create your views here.
def login_view(request):
    context = {
        'title':'BOOK-A-MEAL | LOGIN PAGE'
    }
    return render(request, "login.html", context)


def resetpass_view(request):
    context = {
        'title':'BOOK-A-MEAL | LOGIN PAGE'
    }
    return render(request, "login.html", context)