from rest_framework import serializers
from customer.models import Customer
from menu.models import Menu
from orders.models import Orders
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