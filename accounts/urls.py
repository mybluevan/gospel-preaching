from django.conf.urls import include, url
from django.contrib import auth
from . import views

urlpatterns = [
    url(r'^$', views.profile_list, name='accounts_profile_list'),
    url(r'^register/$', views.register, name='accounts_register'),
    url(r'^profile/$', views.profile_detail, name='accounts_profile_detail_me'),
    url(r'^profile/(?P<username>[a-zA-Z0-9_-]+)/$', views.profile_detail, name='accounts_profile_detail'),
    url(r'^/', include(auth.urls)),
]
