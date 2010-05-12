from django.db import models
from tinymce import models as tinymce_models
from datetime import date
from os.path import exists
from django.contrib.auth.models import User
from django.conf import settings
from decimal import Decimal

def get_filename(instance, filename):
    split = filename.split('.')
    ext = ''.join(['.', split[len(split) - 1]])
    month = ''.join([str(date.today().year), '_', str(date.today().month)])
    fn = ''.join(['simple_orders/products/', month, '/', instance.slug, ext])
    i = 1
    while True:
        if exists(''.join([settings.MEDIA_ROOT, fn])):
            fn = ''.join(['simple_orders/products/', month, '/', instance.slug, '_', str(i), ext])
            i += 1
        else:
            return fn

class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = tinymce_models.HTMLField(blank=True)
    photo = models.ImageField(upload_to=get_filename, null=True, blank=True, max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    qoh = models.IntegerField(verbose_name='quantity on hand')
    class Meta:
        ordering = ['slug']
    @models.permalink
    def get_absolute_url(self):
        return ('simple_orders.views.product_detail', [self.slug])
    def __unicode__(self):
        return self.slug

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True)
    ship_date = models.DateTimeField(verbose_name='date shipped', null=True, blank=True)
    ship_name = models.CharField(verbose_name='shipping name', max_length=200)
    ship_addr = models.CharField(verbose_name='shipping address', max_length=200)
    ship_city = models.CharField(verbose_name='shipping city', max_length=100)
    ship_state = models.CharField(verbose_name='shipping state', max_length=2)
    ship_zip = models.CharField(verbose_name='shipping ZIP', max_length=10)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    instructions = models.TextField(verbose_name='additional instructions', blank=True)
    shipped = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    payment_method = models.CharField(verbose_name='payment method', max_length=2, choices=(('C','Check'),('PP','Paypal')))
    class Meta:
        ordering = ['-date']
    def calc_ship_cost(self, orderitems):
        if orderitems:
            return Decimal('10.00')
        return Decimal('0.00')
    def calc_total(self, orderitems):
        total = self.calc_ship_cost(orderitems)
        for item in orderitems:
            total += (Decimal(item.quantity) * item.product.price)
        return total
    def calc_sub_total(self, orderitems):
        st = 0
        for item in orderitems:
            st += (Decimal(item.quantity) * item.product.price)
        return st
    @property
    def sub_total(self):
        return self.calc_sub_total(self.orderitem_set.all())
    @property
    def total(self):
        return self.calc_total(self.orderitem_set.all())
    @property
    def ship_cost(self):
        return self.calc_ship_cost(self.orderitem_set.all())
    def __unicode__(self):
        return ' '.join([unicode(self.date.date()), self.ship_name])

class OrderItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)
    class Meta:
        verbose_name = "order item"
        ordering = ['-order','product']
    @property
    def product_name(self):
        if self.product and self.product.title:
            return self.product.title
        return 0
    @property
    def price_per(self):
        if self.product and self.product.price:
            return self.product.price
        return 0
    @property
    def price_total(self):
        if self.product and self.product.price:
            return self.product.price * Decimal(self.quantity)
        return 0
    def save(self, *args, **kwargs):
        if self.id:
            old_item = OrderItem.objects.get(pk=self.id)
            self.product.qoh -= (self.quantity - old_item.quantity)
        else:
            self.product.qoh -= self.quantity
        self.product.save()
        super(OrderItem, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        if self.id:
            self.product.qoh += self.quantity
            self.product.save()
        super(OrderItem, self).delete(*args, **kwargs)
    def __unicode__(self):
        return ' '.join([unicode(self.order), '-', unicode(self.product)])
