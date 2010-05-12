from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User

class Question(models.Model):
    qtext = models.TextField(verbose_name='question text')
    date = models.DateTimeField(auto_now_add=True)
    atext = tinymce_models.HTMLField(verbose_name='answer text', blank=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, blank=True)
    email = models.EmailField(blank=True)
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return self.qtext[:144]
