from django.urls import path,re_path
from . import views
urlpatterns=[
  path('create',views.create_menu,name='createmenu'),
  path('',views.menu,name='menu')


]