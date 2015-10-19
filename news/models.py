from django.db import models
from tinymce import models as tinymce_models

class Update(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    text = tinymce_models.HTMLField(blank=True)
    date = models.DateTimeField('date submitted', auto_now_add=True)
    email = models.EmailField()
    approved = models.BooleanField(default=False)
    class Meta:
        ordering = ['-date']
    def get_absolute_url(self):
        return ('news.views.detail', [self.slug])
    def __unicode__(self):
        return self.slug
