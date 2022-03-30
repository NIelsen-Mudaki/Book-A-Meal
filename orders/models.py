from django.db import models
from menu.models import Menu
from customer.models import Customer

# Create your models here.
class Orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    menu_id = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=255,default='pending')
