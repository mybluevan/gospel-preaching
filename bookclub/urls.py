from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.order_create, name='bookclub_order_create'),
    url(r'^list/$', views.order_list, name='bookclub_order_list'),
    #url(r'^join_complete/$', views.join_complete),
    #url(r'^ask/$', views.ask_question),
    #url(r'^(?P<pk>\d+)/$', views.detail),
]
