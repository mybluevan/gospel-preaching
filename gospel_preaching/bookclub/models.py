from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField

class Order(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = USStateField()
    zip_code = models.CharField(max_length=10)
    email = models.EmailField(blank=True)
    phone = PhoneNumberField(blank=True)
    is_cell = models.BooleanField()
    join_bookclub = models.BooleanField()
    commentary_mat = models.IntegerField(null=True, blank=True)
    commentary_mark = models.IntegerField(null=True, blank=True)
    commentary_acts = models.IntegerField(null=True, blank=True)
    commentary_first_cor = models.IntegerField(null=True, blank=True)
    commentary_gal_eph = models.IntegerField(null=True, blank=True)
    commentary_phil_thes = models.IntegerField(null=True, blank=True)
    commentary_tim_philm = models.IntegerField(null=True, blank=True)
    commentary_hebrews = models.IntegerField(null=True, blank=True)
    commentary_james = models.IntegerField(null=True, blank=True)
    commentary_peter_jude = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, related_name='bookclub_orders')
    class Meta:
        ordering = ['-date']
    def __unicode__(self):
        return ''.join([self.name, ": ", unicode(self.date)])
