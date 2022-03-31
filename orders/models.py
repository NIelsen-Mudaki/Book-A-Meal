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
        



    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer_id=customer_id).order_by('order_date')

    @staticmethod
    def get_all_orders():
        return Orders.objects.all().order_by('order_date')

