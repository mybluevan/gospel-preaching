from gospel_preaching.master.models import App
from django.conf import settings
from django.contrib.sites.models import Site

def apps(request):
    app = request.path[1:].split('/', 1)[0]
    try:
        cur_app = App.objects.get(slug=app)
    except App.DoesNotExist:
        cur_app = None
    return {
        'site_apps': App.objects.all(),
        'cur_app': cur_app
    }

def email(request):
    try:
        form_url = settings.ADMIN_EMAIL_FORM_URL
    except AttributeError:
        form_url = ""
    try:
        redir_url = settings.ADMIN_EMAIL_REDIR_URL
    except AttributeError:
        redir_url = ""
    try:
        user = settings.ADMIN_EMAIL_USER
    except AttributeError:
        user = ""
    try:
        passwd = settings.ADMIN_EMAIL_PASSWD
    except AttributeError:
        passwd = ""

    return {
        'admin_email_form_url': form_url,
        'admin_email_redir_url': redir_url,
        'admin_email_user': user,
        'admin_email_passwd': passwd,
    }

def current_site(request):
    # A context processor to add the "current site" to the current Context
    try:
        current_site = Site.objects.get_current()
        return {
            'current_site': current_site,
        }
    except Site.DoesNotExist:
        # always return a dict, no matter what!
        return {'current_site':''} # an empty string
