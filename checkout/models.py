from django.db import models

class Order(models.Model):
    #first_name = models.CharField(max_length=50)
    #last_name = models.CharField(max_length=50)
    #gender = models.CharField(max_length=10, null=True, blank=True)
    #phone = models.CharField(max_length=10)
    #email = models.CharField(max_length=100)
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)
    service = models.ForeignKey('Service', null=True, blank=True, on_delete=models.SET_NULL)
    resource = models.ForeignKey('Resource', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.ForeignKey('CalendarDate', null=True, blank=True, on_delete=models.SET_NULL)
    time = models.ForeignKey('CalendarTime', null=True, blank=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False, null=True, blank=True)