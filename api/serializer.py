from rest_framework import serializers
from customer.models import Customer
from menu.models import Menu
from orders.models import Order, OrderItem, Orders
from api.models import NewsLetter

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id','customer_name', 'email', 'phone', 'is_Customer']
        depth=1

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
        depth=1

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'
        depth=1


class NewsLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        fields = ['email']

class OrderItemSerializer(serializers.ModelSerializer):
    meal=serializers.CharField(source='menu_id.meal',read_only=True)
    class Meta:
        model=OrderItem
        fields=['order','menu_id','quantity','meal']

class MultiOrderSerializer(serializers.ModelSerializer):
    orderitem=OrderItemSerializer(many=True)
    class Meta:
        model=Order
        fields=['id','order_ref','order_date','order_status','order_total_price','orderitem']
        depth=1

