from django.conf.urls.defaults import *

urlpatterns = patterns('bookclub.views',
    (r'^$', 'order'),
    (r'^list/$', 'list_orders'),
    #(r'^join_complete/$', 'join_complete'),
    #(r'^ask/$', 'ask_question'),
    #(r'^(?P<pk>\d+)/$', 'detail'),
)
