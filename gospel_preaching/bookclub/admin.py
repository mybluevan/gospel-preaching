from bookclub.models import Member
from django.contrib import admin

class MemberAdmin(admin.ModelAdmin):
    search_fields = ['name', 'address', 'city', 'state', 'zip_code', 'email', 'phone']
    date_hierarchy = 'date'
    list_display = ('date', 'name', 'address', 'city', 'state', 'zip_code', 'email', 'phone', 'user')
    save_on_top = True
    
admin.site.register(Member, MemberAdmin)
