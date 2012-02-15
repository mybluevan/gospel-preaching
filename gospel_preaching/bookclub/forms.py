from django.forms import ModelForm
from bookclub.models import Member
from django import forms
from django.contrib.localflavor.us.forms import USZipCodeField, USPhoneNumberField

class JoinForm(ModelForm):
    zip_code = USZipCodeField(label='ZIP Code')
    email = forms.EmailField(label='E-mail Address')
    phone = USPhoneNumberField(label='Phone Number')
    commentary_mat = forms.BooleanField(required=False, label='Matthew Commentary (when it is available) - $20.00')
    commentary_mark = forms.BooleanField(required=False, label='Mark Commentary - $15.00')
    commentary_acts = forms.BooleanField(required=False, label='Acts Commentary - $15.00')
    commentary_gal_eph = forms.BooleanField(required=False, label='Galatians/Ephesians Commentary - $15.00')
    commentary_phil_thes = forms.BooleanField(required=False, label='Philippians-Thessalonians Commentary - $15.00')
    commentary_tim_philm = forms.BooleanField(required=False, label='Timothy-Philemon Commentary - $15.00')
    class Meta:
        model = Member
        fields = ('name', 'address', 'city', 'state', 'zip_code', 'email', 'phone', 'commentary_mat', 'commentary_mark', 'commentary_acts', 'commentary_gal_eph', 'commentary_phil_thes', 'commentary_tim_philm')
