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
from login.views import login_view,resetpass_view,logout_view
from caterers.views import manageadmins_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_view, name="logins"),
    path('reset_password/',resetpass_view, name="reset"),
    path('logout_user/',logout_view, name="logout"),
    path('manage-caterers/',manageadmins_view, name="managecaters"),
    path('', include('orders.urls')),
    path('', include('sales.urls')),

]
