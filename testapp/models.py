from django.db import models
from django.utils import timezone

# Create your models here.
from testapp.constants import TIMEZONES


class NameDetails(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    real_name = models.CharField(max_length=32, blank=True, null=True)
    tz = models.CharField(max_length=32, choices=TIMEZONES,default='UTC')

class DateDetails(models.Model):
    namedetails = models.ForeignKey(NameDetails, on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)