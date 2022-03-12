from django.db import models

class Clinician(models.Model):
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    class Meta: 
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

class Service(models.Model):
    clinicians = models.ManyToManyField(Clinician)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta: 
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price)

class ServiceDate(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.date.strftime("%d/%m/%Y")

class ServiceTime(models.Model):
    time = models.TimeField()
   
    def __str__(self):
        return self.time.strftime("%H:%M")

class ServicePage(models.Model):
    service = models.ForeignKey(Service, null=False, blank=False, on_delete=models.CASCADE)
    clinician = models.ForeignKey(Clinician, null=False, blank=False, on_delete=models.CASCADE) 
    date = models.ForeignKey(ServiceDate, null=False, blank=False, on_delete=models.CASCADE)
    time = models.ForeignKey(ServiceTime, null=False, blank=False, on_delete=models.CASCADE)