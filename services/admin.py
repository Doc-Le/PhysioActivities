from django.contrib import admin
from .models import Clinician, Service

# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price'
    )

    ordering = ('name',)


class ClinicianAdmin(admin.ModelAdmin):
    list_display = (
        'full_name',
        'gender',
    )

    ordering = ('full_name',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Clinician, ClinicianAdmin)
