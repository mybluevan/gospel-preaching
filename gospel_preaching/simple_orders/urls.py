from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('simple_orders.views',
    # Example:
    # (r'^gospel_preaching/', include('gospel_preaching.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'product_index'),
    (r'^cart/$', 'update_cart'),
    (r'^cart/checkout/$', 'checkout'),
    (r'^cart/order-confirmation/$', 'order_confirm'),
    (r'^products/(?P<slug>[a-zA-Z0-9_-]+)/add-to-cart/$', 'add_to_cart'),
    (r'^products/(?P<slug>[a-zA-Z0-9_-]+)/$', 'product_detail'),
)
