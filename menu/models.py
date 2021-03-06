from datetime import datetime, timedelta
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
# Create your models here.

class MenuDate(models.Model):
    menu_date=models.DateField()
    class Meta:
        db_table='MenuDate'

    def get_menus_per_date(self):
        return self.menus.all()

class Menu(models.Model):
    meal = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    image = CloudinaryField('image')
    menu_date=models.ManyToManyField(MenuDate,related_name='menus',blank=True)
    created=models.DateTimeField(auto_now=True,null=True)

    class Meta:
        db_table = 'Menu'

    def __str__(self):
        return self.meal


    def add_menu_to_date(self,menu_date):
        self.menu_date.add(menu_date)
        return 

    def remove_menu_from_date(self,menu_date):
        self.menu_date.delete(menu_date)
        print('removed')
        return

    @classmethod
    def get_menu_list_to_assign(cls,assigned_ids):
        return Menu.objects.exclude(id__in=assigned_ids).all()

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

