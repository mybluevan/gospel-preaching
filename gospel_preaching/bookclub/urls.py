from django.conf.urls.defaults import *

urlpatterns = patterns('bookclub.views',
    (r'^$', 'join'),
    #(r'^ask/$', 'ask_question'),
    #(r'^(?P<pk>\d+)/$', 'detail'),
)
