from django.db import models
from menu.models import Menu
from customer.models import Customer

# Create your models here.
class Orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255,default='pending')


    class Meta:
        db_table = 'Orders'

    def __str__(self):
        return self.order_status

    @classmethod
    def get_grand_total(cls):
        orders = Orders.objects.all()
        total = 0
        for order in orders:
            sub_total = order.quantity * order.menu_id.price

            total+= sub_total
        print(total)
        return total
        
    @classmethod
    def search_by_date(cls,search_term):
        orders = cls.objects.filter(order_date__icontains=search_term)
        return orders



    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer_id=customer_id).order_by('order_date')

    @staticmethod
    def get_all_orders():
        return Orders.objects.all().order_by('order_date')

    
class Order(models.Model):
    order_ref=models.CharField(max_length=50,default='AA',unique=True)
    order_date = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(Customer, related_name='order',on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255,default='pending')
    order_total_price=models.FloatField()

    class Meta:
        db_table='order'

    def __str__(self):
        return self.order_status

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='orderitem',on_delete=models.CASCADE)
    menu_id = models.ForeignKey(Menu,related_name="order_item", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table='orderitem'