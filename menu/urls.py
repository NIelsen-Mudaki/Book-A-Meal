from django.urls import path,re_path
from . import views
urlpatterns=[
  path('create',views.create_menu,name='createmenu'),
  re_path('^available/(.*)',views.available,name='available'),
  re_path('^unavailable/(.*)',views.make_unavailable,name='make_unavailable'),
  re_path('delete/(.*)',views.delete_menu,name='delete_menu'),
  re_path('edit/(.*)',views.edit_menu,name='editmenu'),
  path('',views.menu,name='menu')


]