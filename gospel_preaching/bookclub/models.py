from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Member(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = models.CharField(max_length=10)
    email = models.EmailField()
    phone = PhoneNumberField()
    commentary_mat = models.BooleanField()
    commentary_mark = models.BooleanField()
    commentary_acts = models.BooleanField()
    commentary_gal_eph = models.BooleanField()
    commentary_phil_thes = models.BooleanField()
    commentary_tim_philm = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return ''.join([self.name, ": ", unicode(self.date)])
