from django.db import models
from django.core.exceptions import ValidationError

from datetime import datetime

def is_positive(value):
    if value >= 0:
        raise ValidationError(u'%s is not an even number' % value)

CHOICES = (('M','Morning'),('D','Day'),('N','Night'))
class Pullup(models.Model):
    first_set = models.IntegerField(validators=[is_positive])
    second_set = models.IntegerField()
    third_set = models.IntegerField()
    average = models.FloatField()
    total = models.IntegerField()
    time_of_day = models.CharField(max_length=1, choices=CHOICES)
    date = models.DateField(default=datetime.now())
    notes = models.TextField(blank=True)

    def __unicode__(self):
        return str(self.date)

    def save(self, *args, **kwargs):
        self.average = float((self.first_set + self.second_set + self.third_set) / 3)
        self.total = self.first_set + self.second_set + self.third_set
        super(Pullup, self).save(*args, **kwargs)