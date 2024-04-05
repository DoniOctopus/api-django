from django.db import models
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    name = models.TextField(blank=True, null=True)
    identity_number = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    birth_of_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile'
