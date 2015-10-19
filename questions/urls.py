from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.question_list, name='questions_question_list'),
    url(r'^ask/$', views.question_ask, name='questions_question_ask'),
    #url(r'^(?P<pk>\d+)/$', views.question_detail, name='questions_question_detail'),
]
