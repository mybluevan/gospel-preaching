from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('articles.views',
    # Example:
    # (r'^gospel_preaching/', include('gospel_preaching.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    (r'^$', 'index'),
    (r'^ajax/authors/$', 'author_partial'),
    (r'^ajax/tags/$', 'tag_partial'),
    (r'^cat/(?P<slug>[a-zA-Z0-9_-]+)/$', 'cat'),
    (r'^tag/(?P<slug>[a-zA-Z0-9_-]+)/$', 'tag'),
    (r'^author/(?P<slug>[a-zA-Z0-9_-]+)/$', 'author'),
    (r'^remove-comment/(?P<pk>[0-9]+)$', 'remove_comment'),
    (r'^(?P<slug>[a-zA-Z0-9_-]+)/like/$', 'like'),
    (r'^(?P<slug>[a-zA-Z0-9_-]+)/$', 'detail'),
)
