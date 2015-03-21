from django.db import models
from django.template.defaultfilters import slugify

from datetime import datetime

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published', default=datetime.now())
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Gallery, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

class Image(models.Model):
    gallery = models.ForeignKey(Gallery)
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    thumb = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published', default=datetime.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.thumb = self.name[:self.name.rfind('.')] + '_thumb' + self.name[self.name.rfind('.'):]
        super(Image, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name