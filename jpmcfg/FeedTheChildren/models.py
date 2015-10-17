from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
  username = models.ForeignKey(User)
  p_type = models.CharField(max_length=30)
  
class Customers(models.Model):
  snap = models.CharField(max_length=30)
  home_loc = models.CharField(max_length=30)
  distance_rad = models.IntegerField()
  
class Vendor(models.Model):
  store_name = models.CharField(max_length=30)
  location = models.CharField(max_length=30)
  hours = models.CharField(max_length=30)
