from django.forms import ModelForm
from bookclub.models import Order
from django import forms
from django.contrib.localflavor.us.forms import USZipCodeField, USPhoneNumberField

class OrderForm(ModelForm):
    zip_code = USZipCodeField(label='ZIP Code')
    email = forms.EmailField(required=False, label='E-mail Address')
    phone = USPhoneNumberField(required=False, label='Phone Number')
    commentary_mat = forms.IntegerField(required=False, label='Matthew Commentary (when it is available) - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_mark = forms.IntegerField(required=False, label='Mark Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_acts = forms.IntegerField(required=False, label='Acts Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_first_cor = forms.IntegerField(required=False, label='First Corinthians Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_gal_eph = forms.IntegerField(required=False, label='Galatians/Ephesians Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_phil_thes = forms.IntegerField(required=False, label='Philippians-Thessalonians Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_tim_philm = forms.IntegerField(required=False, label='Timothy-Philemon Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_james = forms.IntegerField(required=False, label='James Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_peter_jude = forms.IntegerField(required=False, label='First Peter-Jude Commentary - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    class Meta:
        model = Order
        fields = ('name', 'address', 'city', 'state', 'zip_code', 'email', 'phone', 'commentary_mat', 'commentary_mark', 'commentary_acts', 'commentary_first_cor', 'commentary_gal_eph', 'commentary_phil_thes', 'commentary_tim_philm', 'commentary_james', 'commentary_peter_jude')
