from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from bookclub.forms import JoinForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.conf import settings

def join(request):
    if request.method == 'POST':
        form = JoinForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            if request.user.is_authenticated():
                m.user = request.user
            m.save()
            
            plaintext = get_template('bookclub/join_email.txt')
            context = Context({ 'member': m })
            try:
                addresses = settings.BOOKCLUB_ADMIN_EMAILS
                subject = settings.BOOKCLUB_SUBJECT
                from_address = settings.DEFAULT_FROM_EMAIL
                send_mail(subject, plaintext.render(context), from_address, addresses, fail_silently=True)
            except AttributeError:
                pass
            
            return HttpResponseRedirect(reverse(join_complete))
    else:
        form = JoinForm()
    return render_to_response('bookclub/join.html', {'join_form': form,}, context_instance = RequestContext(request))
    
def join_complete(request):
    return render_to_response('bookclub/join_complete.html', context_instance = RequestContext(request))
