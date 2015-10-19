from django.shortcuts import render_to_response, get_object_or_404
from gospel_preaching.master.models import App
from django.template import RequestContext

def index(request):
    return render_to_response('master/index.html', {}, context_instance = RequestContext(request))
