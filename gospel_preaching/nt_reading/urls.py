from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gospel_preaching/', include('gospel_preaching.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'gospel_preaching.nt_reading.views.index'),
    (r'^(?P<book>[a-zA-Z0-9_-]+)/$', 'gospel_preaching.nt_reading.views.book'),
    (r'^(?P<book>[a-zA-Z0-9_-]+)/(?P<chapter>[0-9]+)/$', 'gospel_preaching.nt_reading.views.chapter'),
)
