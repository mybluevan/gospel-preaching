from django.conf.urls import include, url
from django.conf import settings
from master.models import App
from master import views
from django.contrib import admin
from django.views import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='master_index'),
    #url(r'^socialregistration/', include('socialregistration.urls')),
]

app_list = App.objects.all().exclude(class_name__startswith='none')
for app in app_list:
    urlpatterns += [url(r'^%s/' % (app.slug), include('%s.urls' % (app.class_name), namespace=app.class_name)),]
