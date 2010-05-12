from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout, password_change, password_change_done, password_reset, password_reset_done, password_reset_confirm, password_reset_complete

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('accounts.views',
    # Example:
    # (r'^gospel_preaching/', include('gospel_preaching.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'index'),
    (r'^login/$',  login),
    (r'^logout/$',  logout),
    (r'^password_change/$', password_change),
    (r'^password_change_done/$', password_change_done),
    (r'^password_reset/$', password_reset),
    (r'^password_reset_done/$', password_reset_done),
    (r'^password_reset_confirm/$', password_reset_confirm),
    (r'^password_reset_complete/$', password_reset_complete),
    (r'^register/$', 'register'),
    (r'^profile/$', 'profile'),
    (r'^profile/(?P<username>[a-zA-Z0-9_-]+)/$', 'profile'),
)
