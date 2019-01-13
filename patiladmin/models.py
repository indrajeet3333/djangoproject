from django.db import models
from django.utils import timezone
# Create your models here.
class client(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    email = models.CharField(max_length=255)
    pVisit = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.BigIntegerField()
    dateofvisit = models.DateField(default=timezone.now)

    def __str__(self):
        return (self.first_name + " " + self.last_name)


class appointments(models.Model):
    person = models.CharField(max_length=255)
    dtOfApmt = models.CharField(max_length=255)
    tmOfApmt = models.CharField(max_length=255)
    schOn = models.DateTimeField(default=timezone.now, blank=True)
    class Meta:
        verbose_name_plural = "Appointments"
    def __str__(self):
        return (self.person)
    

    
