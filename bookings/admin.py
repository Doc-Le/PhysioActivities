from django.contrib import admin
from .models import Booking, BookingDate, BookingTime


class BookingAdmin(admin.TabularInline):
    model = Booking

    fields = ('user', 'service', 'clinician', 'date', 'time', 'total',)
    
    readonly_fields = ('datetime', 'total',)
    
    list_display = ('datetime', 'user', 'service', 'clinician', 'total',)

    ordering = ('-datetime',)

class BookingDateAdmin(admin.TabularInline):
    model = BookingDate
    fields = ('date',)
    ordering = ('-date',)

class BookingTimeAdmin(admin.TabularInline):
    model = BookingTime
    fields = ('time',)
    ordering = ('-time',)

admin.site.register(Booking)
admin.site.register(BookingDate)
admin.site.register(BookingTime)