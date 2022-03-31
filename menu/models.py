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
    
    @classmethod
    def get_active_menu_items(cls):
        return cls.objects.filter(status=True).all()


    @classmethod
    def get_inactive_menu_items(cls):
        return cls.objects.filter(status=False).all()


    def change_status(self):
        self.status=not self.status
        self.save()
        return self

    def delete_menu(self):
        self.delete()
        return f"{self} is deleted"

    def edit_menu(self,**kwags):
        for key, value in kwags.items():
            setattr(self,key,value)

        self.save()

        return self

