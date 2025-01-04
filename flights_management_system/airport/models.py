from django.db import models

# Create your models here.
class AIRPORT(models.Model):
    city = models.CharField(max_length=64)
    airport_id = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.city} ({self.airport_id})'
    