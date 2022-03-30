from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Menu(models.Model):
    meal = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    image = CloudinaryField('image')

    class Meta:
        db_table = 'Menu'

    def __str__(self):
        return self.meal
