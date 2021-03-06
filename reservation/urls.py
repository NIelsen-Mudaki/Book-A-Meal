"""reservation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from login.views import login_view,resetpass_view,logout_view,delete_view
from caterers.views import manageadmins_view,editusers_view,updateuser_view
from dashboard.views import dashboard_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/',include('menu.urls')),
    path('',login_view, name="logins"),
    path('reset_password/',resetpass_view, name="reset"),
    path('dashboard/',dashboard_view, name="dashboard"),
    path('logout_user/',logout_view, name="logout"),
    path('delete_user/<int:id>/',delete_view, name="delete"),
    path('manage-caterers/',manageadmins_view, name="managecaters"),
    path('edituser/<int:id>/',editusers_view, name="edituser"),
    path('updateuser/',updateuser_view, name="updateuser"),
    path('', include('orders.urls')),
    path('', include('sales.urls')),
    #api urls
    path('api/',include('api.urls'))

]
