from django import forms
from django.forms.extras.widgets import SelectDateWidget

class Basic_Form(forms.Form):
    date = forms.DateField(widget=SelectDateWidget)
    subject = forms.CharField(max_length=100)
