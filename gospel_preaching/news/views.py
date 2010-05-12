from django.shortcuts import render_to_response, get_object_or_404
from gospel_preaching.news.models import Update
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings

def index(request):
    page = request.GET.get('page', 1)
    try:
        perpage = settings.NEWS_PER_PAGE
    except AttributeError:
        perpage = 10
    pager = Paginator(Update.objects.all(), perpage)
    return render_to_response('news/index.html', {'all_updates': pager.page(page).object_list, 'order': None, 'page': pager.page(page), 'pager': pager}, context_instance = RequestContext(request))

def detail(request, slug):
    u = get_object_or_404(Update, slug__exact=slug)
    return render_to_response('news/detail.html', {'update': u}, context_instance = RequestContext(request))
