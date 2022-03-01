from django.contrib import admin
from .models import Order, Booking


class BookingAdmin(admin.TabularInline):
    model = Booking

    fields = ('datetime', 'service', 'clinician', 'total',)
    
    readonly_fields = ('total',)
    
    list_display = ('datetime', 'service', 'clinician', 'total',)

    ordering = ('-datetime',)

class OrderAdmin(admin.ModelAdmin):
    inlines = (BookingAdmin,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Booking)
admin.site.register(Order, OrderAdmin)
