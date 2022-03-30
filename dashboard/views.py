from django.shortcuts import render

# Create your views here.
def dashboard_view(request):
    context = {
        'title' : 'BOOK-A-MEAL | DASHBOARD',
    }
    return render(request, "dashboard.html",context)