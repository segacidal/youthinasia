from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

from datetime import datetime

def is_positive(value):
    if value <= 0:
        raise ValidationError(u'%s is not a positive integer.' % value)

'''
A routine is a set of Days, For example, Push-Pull-Legs, or A-B-A
Should have a good description (hypertrophy, strength, etc.)
(to be added later)
'''
class Routine(models.Model):
    pass

'''
A Day is a set of Exercises. For example, "leg day", or simply "A"
in an "ABxABxx" workout.
'''
class Day(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.now())
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Day, self).save(*args, **kwargs)

class Exercise(models.Model):
    days = models.ManyToManyField(Day)
    name = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.now())
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Exercise, self).save(*args, **kwargs)

class Instance(models.Model):
    name = models.CharField(max_length=50, blank=True, editable=False)
    exercise = models.ForeignKey(Exercise)
    weight = models.FloatField()
    reps = models.IntegerField(validators=[is_positive])
    sets = models.IntegerField(validators=[is_positive])
    date = models.DateField(default=datetime.now())

    def save(self, *args, **kwargs):
        self.name = '<Instance ID #%s>' % (self.pk)
        super(Instance, self).save(*args, **kwargs)

    def __str__(self):
        return self.name