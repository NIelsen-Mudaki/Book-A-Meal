from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=300)
    is_Caterer = models.BooleanField(default=False)
    is_Customer = models.BooleanField(default=False)
    
    
    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return self.customer_name