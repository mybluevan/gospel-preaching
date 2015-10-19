from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='articles_article_list'),
    url(r'^ajax/authors/$', views.author_partial, name='articles_author_partial'),
    url(r'^ajax/tags/$', views.tag_partial, name='articles_tag_partial'),
    url(r'^cat/(?P<slug>[a-zA-Z0-9_-]+)/$', views.category_detail, name='articles_category_detail'),
    url(r'^tag/(?P<slug>[a-zA-Z0-9_-]+)/$', views.tag_detail, name='articles_tag_detail'),
    url(r'^author/(?P<slug>[a-zA-Z0-9_-]+)/$', views.author_detail, name='articles_author_detail'),
    url(r'^remove-comment/(?P<pk>[0-9]+)$', views.comment_remove, name='articles_comment_remove'),
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)/like/$', views.article_like, name='articles_article_like'),
    url(r'^(?P<slug>[a-zA-Z0-9_-]+)/$', views.article_detail, name='articles_article_detail'),
]
