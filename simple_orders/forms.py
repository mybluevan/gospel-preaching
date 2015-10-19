from django.forms import ModelForm, IntegerField
from django.forms.formsets import formset_factory
from calc_fields import CalcForm, CalcFormSet
from simple_orders.models import Order

class OrderForm(ModelForm):
    class Meta:
        exclude = ('user', 'ship_date', 'shipped', 'paid')
        model = Order

class OrderItemForm(CalcForm):
    quantity = IntegerField()
    calc_defs = {'name': ('product_name',''), 'price_each': ('price_per','$%#.2f'), 'total_price': ('price_total','$%#.2f')}
    fields = ('name', 'quantity', 'price_each', 'total_price')
    def __init__(self, instance=None, *args, **kwargs):
        if instance:
            initial = {'quantity': instance.quantity}
            super(OrderItemForm, self).__init__(instance=instance, initial=initial, *args, **kwargs)
        else:
            super(OrderItemForm, self).__init__(*args, **kwargs)

OrderItemFormSet = formset_factory(OrderItemForm, formset=CalcFormSet, extra=0, can_delete=True)
