from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.TabularInline):
    model = Booking

    fields = ('datetime', 'user', 'service', 'clinician', 'total',)
    
    readonly_fields = ('total',)
    
    list_display = ('datetime', 'user', 'service', 'clinician', 'total',)

    ordering = ('-datetime',)

admin.site.register(Booking)
