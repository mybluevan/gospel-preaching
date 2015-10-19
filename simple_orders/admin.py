from models import Product, Order, OrderItem
from django.contrib import admin
from datetime import date
from calc_fields import CalcAdmin

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 10

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'description']
    list_display = ('title', 'price', 'qoh')

class OrderAdmin(CalcAdmin):
    calc_defs = {'shipping_cost': ('ship_cost','$%#.2f'), 'total': ('total','$%#.2f')}
    fields = ('user', 'ship_date', 'ship_name', 'ship_addr', 'ship_city', 'ship_state', 'ship_zip', 'phone', 'email', 'instructions', 'shipped', 'paid', 'payment_method')
    calc_fields = fields + ('shipping_cost', 'total')
    date_hierarchy = 'date'
    list_display = ('date', 'ship_name', 'phone', 'email', 'shipped', 'paid', 'total')
    list_filter = ('shipped', 'paid')
    actions = ['mark_shipped', 'mark_paid']
    inlines = [OrderItemInline]
    save_on_top = True
    def mark_shipped(self, request, queryset):
        rows_updated = queryset.update(shipped=True, ship_date=date.today())
        if rows_updated == 1:
            message_bit = "1 order was"
        else:
            message_bit = "%s orders were" % rows_updated
        self.message_user(request, "%s successfully marked as shipped." % message_bit)
    mark_shipped.short_description = "Mark selected orders as shipped"
    def mark_paid(self, request, queryset):
        rows_updated = queryset.update(paid=True)
        if rows_updated == 1:
            message_bit = "1 order was"
        else:
            message_bit = "%s orders were" % rows_updated
        self.message_user(request, "%s successfully marked as paid." % message_bit)
    mark_paid.short_description = "Mark selected orders as paid"

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
