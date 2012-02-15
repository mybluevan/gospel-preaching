from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from bookclub.forms import JoinForm
from django.template import RequestContext
from django.core.urlresolvers import reverse

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated():
                m = form.save(commit=False)
                m.user = request.user
                m.save()
            else:
                form.save()
            return HttpResponseRedirect(reverse(join_complete))
    else:
        form = JoinForm()
    return render_to_response('bookclub/join.html', {'join_form': form,}, context_instance = RequestContext(request))
    
def join_complete(request):
    return render_to_response('bookclub/join_complete.html', context_instance = RequestContext(request))
