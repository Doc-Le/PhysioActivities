from django.contrib import admin
from .models import Clinician, Service, ServiceDate, ServiceTime

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


class ServiceDateAdmin(admin.ModelAdmin):
    model = ServiceDate
    fields = ('date',)
    ordering = ('-date',)


class ServiceTimeAdmin(admin.ModelAdmin):
    model = ServiceTime
    fields = ('time',)
    ordering = ('-time',)


admin.site.register(Service, ServiceAdmin)
admin.site.register(Clinician, ClinicianAdmin)
admin.site.register(ServiceDate, ServiceDateAdmin)
admin.site.register(ServiceTime, ServiceTimeAdmin)
