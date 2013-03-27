from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from bookclub.forms import OrderForm
from bookclub.models import Order
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
    try:
        status_page = settings.BOOKCLUB_STATUS_PAGE
    except AttributeError:
        status_page = ''
    return render_to_response('bookclub/order.html', {'order_form': form, 'status_page': status_page,}, context_instance = RequestContext(request))

def list_orders(request):
    if request.user.is_authenticated() and request.user.is_staff:
        return render_to_response('bookclub/order_list.html', {'orders': Order.objects.all(),}, context_instance = RequestContext(request))
    else: raise Http404