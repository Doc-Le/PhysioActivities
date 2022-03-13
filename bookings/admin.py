from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.TabularInline):
    model = Booking

    fields = ('user', 'service', 'clinician', 'date', 'time', 'total',)

    readonly_fields = ('datetime', 'total',)

    list_display = ('datetime', 'user', 'service', 'clinician', 'total',)

    ordering = ('-datetime',)


admin.site.register(Booking)
