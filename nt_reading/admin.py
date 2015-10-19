from gospel_preaching.nt_reading.models import Chapter, Book
from django.contrib import admin

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 30

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ChapterInline]

class ChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'chapter')
    list_filter = ['book']

admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Book, BookAdmin)
