from gospel_preaching.master.models import App

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
