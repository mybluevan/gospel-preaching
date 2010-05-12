from gospel_preaching.news.models import Update
from django.contrib import admin

class UpdateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'text']
    date_hierarchy = 'date'
    list_display = ('title', 'date')

admin.site.register(Update, UpdateAdmin)
