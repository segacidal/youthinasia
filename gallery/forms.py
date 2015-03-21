__author__ = 'clint'

from gallery.models import Gallery, Image

from django import forms

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'notes']