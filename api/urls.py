from webbrowser import get
from django import views
from django.urls import path, re_path
from api.views import get_orders,get_menu,signup,create_order,get_customer_order,reset_password,login,getuser,signupnewslater,get_fiewmenu

#urls
urlpatterns = [
    path('orders/',get_orders),
    path('menu/',get_menu),
    path('signup', signup),
    path('login', login),
    path('user/', getuser),
    path('orders/create/',create_order),
    re_path('customer/(.*)/orders/',get_customer_order),
    path('reset/password',reset_password),
    path('newsletter/',signupnewslater),
    path('getfiewmenu/',get_fiewmenu)
]