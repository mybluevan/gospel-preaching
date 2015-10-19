from django.db import models
from tinymce import models as tinymce_models

class App(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField(unique=True)
    categories = models.BooleanField('categories?')
    description = tinymce_models.HTMLField(blank=True)
    class Meta:
        ordering = ['order']
    def __unicode__(self):
        return self.title
