from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.update_list, name='news_update_list'),
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$', views.update_detail, name='news_update_detail'),
]
