__author__ = 'clint'

from pullups.models import Pullup

from django import forms

class PullupForm(forms.ModelForm):
    class Meta:
        model = Pullup
        exclude = ('average','total',)