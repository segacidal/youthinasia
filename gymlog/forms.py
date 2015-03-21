from gymlog.models import Instance

from django import forms

class InstanceForm(forms.ModelForm):
    class Meta:
        model = Instance
        exclude = ('name','exercise','date',)