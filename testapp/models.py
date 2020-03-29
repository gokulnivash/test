from django.db import models
from django.utils import timezone

# Create your models here.

class NameDetails(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    real_name = models.CharField(max_length=32, blank=True, null=True)
    tz = models.DateTimeField(auto_now_add=True)
    activity = models.TextField(max_length=500,blank=True,null=True)
