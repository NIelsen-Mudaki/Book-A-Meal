from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('orders/', views.orders,name='orders'),
    path('order-history/', views.order_history,name='order_history'),
    #path('search/', views.search_results, name='search_results'),
]