from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.product_list, name='simple_orders_product_list'),
    url(r'^cart/$', views.cart_detail, name='simple_orders_cart_detail'),
    url(r'^cart/checkout/$', views.cart_checkout, name='simple_orders_cart_checkout'),
    url(r'^cart/order-confirmation/$', views.order_confirm, name='simple_orders_order_confirm'),
    url(r'^products/(?P<slug>[a-zA-Z0-9_-]+)/add-to-cart/$', views.product_add_to_cart, name='simple_orders_product_add_to_cart'),
    url(r'^products/(?P<slug>[a-zA-Z0-9_-]+)/$', views.product_detail, name='simple_orders_product_detail'),
]
