from django.conf.urls.defaults import *
from django.conf import settings
from master.models import App

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^gospel_preaching/', include('gospel_preaching.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'master.views.index'),
#    (r'^socialregistration/', include('socialregistration.urls')),
)

if settings.STATIC_MEDIA_SERVER:
    urlpatterns += patterns('',(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

app_list = App.objects.all().exclude(class_name__startswith='none')
for app in app_list:
    urlpatterns += patterns('',(r'^%s/' % (app.slug), include('%s.urls' % (app.class_name))))
