from django.db import models
import os, os.path
from tinymce import models as tinymce_models
from django.conf import settings

def get_filename(instance, filename):
    split = filename.split('.')
    ext = ''.join(['.', split[len(split) - 1]])
    fn = ''.join(['nt_reading/', instance.book.slug, '/', instance.book.slug, '_', str(instance.chapter), ext])
    if instance.audio:
        instance.audio.delete()
    if os.path.exists(''.join([settings.MEDIA_ROOT, fn])):
        os.remove(''.join([settings.MEDIA_ROOT, fn]))
    return fn

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True)
    order = models.PositiveSmallIntegerField(unique=True)
    class Meta:
        ordering = ['order']
    def __unicode__(self):
        return self.title

class Chapter(models.Model):
    book = models.ForeignKey(Book)
    chapter = models.PositiveSmallIntegerField()
    text = tinymce_models.HTMLField(blank=True)
    audio = models.FileField(upload_to=get_filename, null=True, blank=True)
    prev = models.OneToOneField('self', related_name='next', null=True, blank=True)
    class Meta:
        ordering = ['book__order','chapter']
        unique_together = (("book", "chapter"),)
    def __unicode__(self):
        return ''.join([self.book.slug, '_', str(self.chapter)])
