from articles.models import Article, Audio, Video, Document, OtherMedia, Category, Author, Tag, Comment, Like
from django.contrib import admin

class LikeInline(admin.TabularInline):
    model = Like
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class AudioInline(admin.TabularInline):
    model = Audio
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    extra = 1

class DocInline(admin.TabularInline):
    model = Document
    extra = 1

class OtherInline(admin.TabularInline):
    model = OtherMedia
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)
    search_fields = ['title', 'text']
    date_hierarchy = 'date'
    list_display = ('title', 'author', 'cat', 'date', 'orig_date')
    inlines = [AudioInline, VideoInline, DocInline, OtherInline, CommentInline, LikeInline]
    save_on_top = True

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ('date', 'article', 'user')
    date_hierarchy = 'date'
    search_fields = ['text']

class LikeAdmin(admin.ModelAdmin):
    list_display = ('date', 'article', 'user')
    date_hierarchy = 'date'

class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent')

admin.site.register(Article, ArticleAdmin)
admin.site.register(Audio, MediaAdmin)
admin.site.register(Video, MediaAdmin)
admin.site.register(Document, MediaAdmin)
admin.site.register(OtherMedia, MediaAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
