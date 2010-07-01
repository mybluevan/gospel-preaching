from gospel_preaching.news.models import Update
from django.contrib import admin

class UpdateAdmin(admin.ModelAdmin):
    search_fields = ['title', 'text']
    date_hierarchy = 'date'
    list_display = ('title', 'date', 'email', 'approved')
    list_filter = ('approved')
    actions = ['mark_approved',]
    def mark_approved(self, request, queryset):
        rows_updated = queryset.update(approved=True, ship_date=date.today())
        if rows_updated == 1:
            message_bit = "1 order was"
        else:
            message_bit = "%s orders were" % rows_updated
        self.message_user(request, "%s successfully marked as shipped." % message_bit)
    mark_shipped.short_description = "Mark selected orders as shipped"

admin.site.register(Update, UpdateAdmin)
