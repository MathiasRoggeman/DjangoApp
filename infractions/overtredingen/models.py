from django.db import models

# Create your models here.
class infraction(models.Model):
    street = models.CharField(max_length=200)
    speed_limit= models.CharField(max_length=200)
    infractions_speed= models.CharField(max_length=200)