from django.db import models

# Create your models here.
class client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    email = models.CharField(max_length=50)
    pVisit = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.BigIntegerField()
    dateofvisit = models.DateField()
    
    def __str__(self):
        return (self.first_name + " " + self.last_name)
    
