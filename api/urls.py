from django.urls import path, re_path

from api.views import create_multi_item_order, get_multi_item_orders, get_orders,get_menu,signup,create_order,get_customer_order,reset_password,login,getuser,signupnewslater,get_fiewmenu,get_user_orders
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view
# schema_view=get_swagger_view(title='Book A Meal API')
#urls

from django.views.generic import TemplateView
urlpatterns = [
    path('orders/',get_orders),
    path('ordersmulti/',get_multi_item_orders),
    re_path('user/(.*)/orders/',get_user_orders),
    path('menu/',get_menu),
    path('signup', signup),
    path('login', login),
    path('user/', getuser),
    path('orders/create/',create_order),
    path('orders/createmulti/',create_multi_item_order),
    re_path('customer/(.*)/orders/',get_customer_order),
    path('reset/password',reset_password),
    path('newsletter/',signupnewslater),
    path('getfiewmenu/',get_fiewmenu),
    path('',get_schema_view(

        title="Brasserie Book a meal",
        description="Developer integration documentation"
    ),name='api-schema'),
    path('docs',TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'api-schema'}
    ),name='swagger-ui')
]