from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.book_list, name='nt_reading_book_list'),
    url(r'^(?P<book>[a-zA-Z0-9_-]+)/$', views.book_detail, name='nt_reading_book_detail'),
    url(r'^(?P<book>[a-zA-Z0-9_-]+)/(?P<chapter>[0-9]+)/$', views.chapter_detail, name='nt_reading_chapter_detail'),
]
