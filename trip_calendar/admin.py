from django.contrib import admin

from trip_calendar.models import Calendar, Event

# Register your models here.
admin.site.register(Calendar)
admin.site.register(Event)
