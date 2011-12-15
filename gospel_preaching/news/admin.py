from gospel_preaching.news.models import Update
from django.contrib import admin

class UpdateAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'text']
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'email', 'approved')
    list_filter = ('approved')
    actions = ['mark_approved',]
    def mark_approved(self, request, queryset):
        rows_updated = queryset.update(approved=True)
        if rows_updated == 1:
            message_bit = "1 update was"
        else:
            message_bit = "%s updates were" % rows_updated
        self.message_user(request, "%s successfully approved." % message_bit)
    mark_approved.short_description = "Approve selected news updates"

admin.site.register(Update, UpdateAdmin)
