from webbrowser import get
from django import views
from django.urls import path, re_path
from api.views import get_orders,get_menu,signup,create_order,get_customer_order,reset_password,login

#urls
urlpatterns = [
    path('orders/',get_orders),
    path('menu/',get_menu),
    path('signup', signup),
    path('login', login),
    path('orders/create/',create_order),
    re_path('customer/(.*)/orders/',get_customer_order),
    path('reset/password',reset_password)
]