from django.db import models
from flights.models import FLIGHTS
# Create your models here.
class PASSENGER(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flight = models.ForeignKey(FLIGHTS,on_delete=models.CASCADE,null=True,related_name='passenger')

    def __str__(self):
        return f'{self.first} {self.last}'