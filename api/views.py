from django.shortcuts import render
from customer.models import Customer
from menu.models import Menu,MenuDate
from orders.models import Orders
from api.serializer import *
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
import datetime
from rest_framework import status

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


@api_view(['POST'])
def create_order(request):
    serializers=OrdersSerializer(data=request.data)
    customerid=request.data.get('customer_id')
    target_customer=Customer.objects.filter(id=customerid).first()
    menuid=request.data.get('menu_id')
    target_menu=Menu.objects.filter(id=menuid).first()
    if serializers.is_valid():
        serializers.save(customer_id=target_customer,menu_id=target_menu)
        return Response(serializers.data,status=status.HTTP_201_CREATED)

    return serializers
@api_view(['POST'])
def signup(request):
    customer = request.data
    customer_name = customer['customername']
    email = customer['useremail']
    phone = customer['contact']
    password = customer['password']
    

    user_exists = Customer.objects.filter(email=email)
    if user_exists.exists():
        return Response('User with this e-mail already exists!')
    else:
        hashed_password = make_password(password)
        new_user = Customer(customer_name=customer_name,
                            email=email,
                            phone=phone,
                            password=hashed_password,
                            is_Customer=True,
                            is_Caterer=False)

        new_user.save()
        return Response('Account created successfully!')
