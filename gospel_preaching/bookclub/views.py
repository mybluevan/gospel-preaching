from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from bookclub.forms import OrderForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from django.conf import settings

def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            o = form.save(commit=False)
            if request.user.is_authenticated():
                o.user = request.user
            o.save()
            
            plaintext = get_template('bookclub/order_email.txt')
            context = Context({ 'order': o })
            try:
                addresses = settings.BOOKCLUB_ADMIN_EMAILS
                subject = settings.BOOKCLUB_SUBJECT
                from_address = settings.DEFAULT_FROM_EMAIL
                send_mail(subject, plaintext.render(context), from_address, addresses, fail_silently=True)
                
                return HttpResponseRedirect(settings.BOOKCLUB_REDIRECT)
            except AttributeError:
                return HttpResponseRedirect(reverse(order))
    else:
        form = OrderForm()
    return render_to_response('bookclub/order.html', {'order_form': form,}, context_instance = RequestContext(request))
