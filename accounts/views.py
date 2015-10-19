from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from accounts.forms import NewUserForm, EditProfileForm
from django.template import RequestContext
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.views import login
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import PasswordChangeForm

def profile_list(request):
    page = request.GET.get('page', 1)
    try:
        perpage = settings.USERS_PER_PAGE
    except AttributeError:
        perpage = 10
    pager = Paginator(User.objects.filter(is_active=True).order_by('username'), perpage)
    return render_to_response('registration/index.html', {'users': pager.page(page).object_list,}, context_instance = RequestContext(request))

def profile_detail(request, username=None):
    form = None
    if not username:
        if request.user.is_authenticated():
            u = request.user
            if request.method == 'POST':
                form = EditProfileForm(request.POST, instance=u)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect(reverse(profile))
            else:
                form = EditProfileForm(instance=u)
        else: raise Http404
    else:
        u = get_object_or_404(User, username__exact=username)
    return render_to_response('registration/profile.html', {'user': u, 'form': form}, context_instance = RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            u = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'])
            u.first_name = form.cleaned_data['first_name']
            u.last_name = form.cleaned_data['last_name']
            u.is_active = False
            u.save()
            return HttpResponseRedirect(reverse('articles.views.index'))
    else:
        form = NewUserForm()
    return render_to_response('registration/register.html', {'form': form}, context_instance = RequestContext(request))
