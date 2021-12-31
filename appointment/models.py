import datetime
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    file = models.FileField(upload_to="service_files/", blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name
    
    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

class Resource(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + " " + self.last_name

class ResourceService(models.Model):
    resource = models.ForeignKey(Resource, default=None, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.resource) + " ~ " + str(self.service)

class CalendarDate(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

class CalendarTime(models.Model):
    hour = models.CharField(max_length=2)
    minute = models.CharField(max_length=2)
    
    def __str__(self):
            return self.hour + ":" + self.minute

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    location = models.ForeignKey('Location', null=True, blank=True, on_delete=models.SET_NULL)
    service = models.ForeignKey('Service', null=True, blank=True, on_delete=models.SET_NULL)
    resource = models.ForeignKey('Resource', null=True, blank=True, on_delete=models.SET_NULL)
    date = models.ForeignKey('CalendarDate', null=True, blank=True, on_delete=models.SET_NULL)
    time = models.ForeignKey('CalendarTime', null=True, blank=True, on_delete=models.SET_NULL)
    paid = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name