from django.urls import path,re_path
from . import views
urlpatterns=[
  path('create',views.create_menu,name='createmenu'),
  re_path('available/(.*)',views.available,name='available'),
  re_path('delete/(.*)',views.delete_menu,name='delete_menu'),
  path('',views.menu,name='menu')


]