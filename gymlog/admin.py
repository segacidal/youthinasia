from django.contrib import admin
from gymlog.models import Day, Exercise, Instance

admin.site.register(Day)
admin.site.register(Exercise)
admin.site.register(Instance)

class DayAdmin(admin.ModelAdmin):
    exclude = ('slug','date_created',)