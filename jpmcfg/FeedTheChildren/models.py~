from django.db import models
from django.contrib.auth.models import User

  
class Customers(models.Model):
  snap = models.CharField(max_length=30)
  home_loc = models.CharField(max_length=30)
  distance_rad = models.IntegerField()
  username = models.ForeignKey(User)
  
class Vendor(models.Model):
  store_name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  hours = models.CharField(max_length=30)
  username = models.ForeignKey(User)
