from django.db import models
from tinymce import models as tinymce_models

class Update(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    text = tinymce_models.HTMLField(blank=True)
    date = models.DateTimeField('date published', auto_now_add=True)
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return self.title
