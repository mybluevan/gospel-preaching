from django.forms import ModelForm
from bookclub.models import Order
from django import forms
from django.contrib.localflavor.us.forms import USZipCodeField, USPhoneNumberField

class OrderForm(ModelForm):
    zip_code = USZipCodeField(label='ZIP Code')
    email = forms.EmailField(required=False, label='E-mail Address')
    phone = USPhoneNumberField(required=False, label='Phone Number')
    is_cell = forms.BooleanField(required=False, label='Is this number a cell phone, and can we reach you via text message?')
    join_bookclub = forms.BooleanField(required=False, label='JOIN THE BOOKCLUB - Please send me each volume as they become available.')
    commentary_mat = forms.IntegerField(required=False, label='Matthew Commentary - Written by Mike Criswell - (Available Spring 2012) - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_mark = forms.IntegerField(required=False, label='Mark Commentary - Written by Carl Johnson - In Stock - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_acts = forms.IntegerField(required=False, label='Acts Commentary - Written by Joe Hisle - In Stock - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_first_cor = forms.IntegerField(required=False, label='First Corinthians Commentary - Written by Mark Bailey - Being reprinted - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_gal_eph = forms.IntegerField(required=False, label='Galatians/Ephesians Commentary - Written by Bennie Cryer and Glen Osburn - In Stock - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_phil_thes = forms.IntegerField(required=False, label='Philippians-Thessalonians Commentary - Written by various authors - Being reprinted - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_tim_philm = forms.IntegerField(required=False, label='Timothy-Philemon Commentary - Written by various authors - In Stock - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_hebrews = forms.IntegerField(required=False, label='Hebrews Commentary - Written by Mark Bailey - (Available Fall of 2012) - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_james = forms.IntegerField(required=False, label='James Commentary - Written by Doug Edwards - Being Reprinted - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    commentary_peter_jude = forms.IntegerField(required=False, label='First Peter-Jude Commentary - Written by various authors - Being Reprinted - $20.00', widget=forms.TextInput(attrs={'size': 2,}))
    class Meta:
        model = Order
        fields = ('name', 'address', 'city', 'state', 'zip_code', 'email', 'phone', 'is_cell', 'commentary_mat', 'commentary_mark', 'commentary_acts', 'commentary_first_cor', 'commentary_gal_eph', 'commentary_phil_thes', 'commentary_tim_philm', 'commentary_hebrews', 'commentary_james', 'commentary_peter_jude', 'join_bookclub')
