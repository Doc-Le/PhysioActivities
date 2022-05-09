from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    model = Booking
    
    def patient(self, obj: Booking) -> str:
        return obj.user.fullname()

    fields = ('user', 'service', 'clinician', 'date', 'time', 'total',)

    readonly_fields = ('datetime', 'total',)

    list_display = ('datetime', 'booking_number', 'patient', 'service', 'clinician', 'total',)

    ordering = ('-datetime',)


admin.site.register(Booking, BookingAdmin)
