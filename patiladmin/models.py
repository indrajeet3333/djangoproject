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
    

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
