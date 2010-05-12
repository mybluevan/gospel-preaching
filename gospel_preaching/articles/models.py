from django.db import models
from datetime import date
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from os.path import exists
from django.conf import settings

def get_filename(instance, filename):
    split = filename.split('.')
    ext = ''.join(['.', split[len(split) - 1]])
    month = ''.join([str(date.today().year), '_', str(date.today().month)])
    if isinstance(instance, Author):
        slug = instance.slug[:50]
    else:
        slug = instance.parent.slug
    t = (None,"audio")[isinstance(instance, Audio)]
    t = (t,"video")[isinstance(instance, Video)]
    t = (t,"docs")[isinstance(instance, Document)]
    t = (t,"other")[isinstance(instance, OtherMedia)]
    t = (t,"author")[isinstance(instance, Author)]
    fn = ''.join(['article/', t, '/', month, '/', slug, ext])
    i = 1
    while True:
        if exists(''.join([settings.MEDIA_ROOT, fn])):
            fn = ''.join(['article/', t, '/', month, '/', slug, '_', str(i), ext])
            i += 1
        else:
            return fn

def convert_youtube(url):
    sep = url.find('?v=')
    if sep > 0:
        url = 'http://www.youtube.com/v/%s' % url[sep + 3:]
    sep = url.find('&')
    if sep > 0:
        url = url[:sep]
    return url

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = tinymce_models.HTMLField(blank=True)
    class Meta:
        verbose_name_plural = "categories"
        ordering = ['slug']
    @models.permalink
    def get_absolute_url(self):
        return ('articles.views.cat', [self.slug])
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    bio = tinymce_models.HTMLField(blank=True)
    photo = models.ImageField(upload_to=get_filename, null=True, blank=True, max_length=200)
    class Meta:
        ordering = ['slug']
    @models.permalink
    def get_absolute_url(self):
        return ('articles.views.author', [self.slug])
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    class Meta:
        ordering = ['slug']
    @models.permalink
    def get_absolute_url(self):
        return ('articles.views.tag', [self.slug])
    def __unicode__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    cat = models.ForeignKey(Category, verbose_name='category')
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, related_name='article_set', blank=True)
    text = tinymce_models.HTMLField(blank=True)
    date = models.DateTimeField(verbose_name='date published', auto_now_add=True)
    orig_date = models.DateField(verbose_name='date originally created')
    class Meta:
        ordering = ['-date']
    @models.permalink
    def get_absolute_url(self):
        return ('articles.views.detail', None, {'slug': self.slug})
    def __unicode__(self):
        return self.slug

class Audio(models.Model):
    parent = models.ForeignKey(Article)
    title = models.CharField(max_length=200)
    src = models.FileField(upload_to=get_filename, max_length=200, verbose_name='file')
    class Meta:
        verbose_name_plural = "audio"
        ordering = ['parent__date','title']
    def __unicode__(self):
        return ''.join([unicode(self.parent), "/", self.title])

class Video(models.Model):
    parent = models.ForeignKey(Article)
    title = models.CharField(max_length=200)
    src = models.FileField(upload_to=get_filename, max_length=200, verbose_name='file', blank=True)
    player = models.BooleanField(verbose_name='show player')
    url = models.URLField(blank=True, verbose_name='YouTube URL')
    class Meta:
        ordering = ['parent','title']
    def save(self):
        self.url = convert_youtube(self.url)
        super(Video, self).save()
    def __unicode__(self):
        return ''.join([unicode(self.parent), "/", self.title])

class Document(models.Model):
    parent = models.ForeignKey(Article)
    title = models.CharField(max_length=200)
    src = models.FileField(upload_to=get_filename, max_length=200, verbose_name='file')
    class Meta:
        ordering = ['parent','title']
    def __unicode__(self):
        return ''.join([unicode(self.parent), "/", self.title])

class OtherMedia(models.Model):
    parent = models.ForeignKey(Article)
    title = models.CharField(max_length=200)
    src = models.FileField(upload_to=get_filename, max_length=200, verbose_name='file')
    class Meta:
        verbose_name = "other media"
        verbose_name_plural = "other media"
        ordering = ['parent','title']
    def __unicode__(self):
        return ''.join([unicode(self.parent), "/", self.title])

class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    text = models.TextField()
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return ' '.join([unicode(self.article), unicode(self.date)])

class Like(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)
    user = models.ForeignKey(User)
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return ' '.join([unicode(self.article), unicode(self.date)])
