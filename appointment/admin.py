from django.contrib import admin
from .models import Resource, Appointment, CalendarDate, CalendarTime, Location, ResourceService, Service


admin.site.register(Location)
admin.site.register(Service)
admin.site.register(Resource)
admin.site.register(ResourceService)
admin.site.register(CalendarDate)
admin.site.register(CalendarTime)
admin.site.register(Appointment)
