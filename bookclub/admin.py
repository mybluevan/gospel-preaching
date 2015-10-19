from bookclub.models import Order
from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    search_fields = ['name', 'address', 'city', 'state', 'zip_code', 'email', 'phone']
    date_hierarchy = 'date'
    list_display = ('date', 'name', 'address', 'city', 'state', 'zip_code', 'email', 'phone', 'user')
    save_on_top = True
    
admin.site.register(Order, OrderAdmin)
