from django.db import models
from airport.models import AIRPORT

# Create your models here.
class FLIGHTS(models.Model):
    origin = models.ForeignKey(AIRPORT,on_delete=models.CASCADE,related_name='takeoff')
    destination = models.ForeignKey(AIRPORT,on_delete=models.CASCADE,related_name='land')
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.origin} to {self.destination} : {self.duration}min'

  