from questions.models import Question
from django.contrib import admin

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['qtext', 'atext']
    date_hierarchy = 'date'
    list_display = ('qtext', 'date', 'user', 'email', 'published')
    list_filter = ('published',)
    save_on_top = True

admin.site.register(Question, QuestionAdmin)
