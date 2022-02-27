from django.contrib import admin

import services
from .models import clinicians, services

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price'
    )

    ordering = ('sku',)


class ClinicianAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(services, ServiceAdmin)
admin.site.register(clinicians, ClinicianAdmin)
