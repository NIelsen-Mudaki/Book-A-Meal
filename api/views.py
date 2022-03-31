from django.shortcuts import render
from customer.models import Customer
from menu.models import Menu,MenuDate
from orders.models import Orders
from api.serializer import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime

# Create your views here.

@api_view(['GET'])
def get_orders(request):
    orders = Orders.objects.all()
    if orders:
        serialize = OrdersSerializer(orders,many=True)
        return Response(serialize.data)
    else:
        return Response({})

@api_view(['GET'])
def get_menu(request):
    menu_date = datetime.datetime.today()
    current_menu_date = MenuDate.objects.filter(menu_date=menu_date).first()
    menus = current_menu_date.menus.all()
    if menus:
        serialize = MenuSerializer(menus, many=True)
        return Response(serialize.data)
    else:
        return Response({})