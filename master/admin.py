from gospel_preaching.master.models import App
from django.contrib import admin

class AppAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order', 'categories')

admin.site.register(App, AppAdmin)
