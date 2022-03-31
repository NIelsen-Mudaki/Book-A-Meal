from webbrowser import get
from django import views
from django.urls import path
from api.views import get_orders,get_menu

#urls
urlpatterns = [
    path('orders/',get_orders),
    path('menu/',get_menu)
]