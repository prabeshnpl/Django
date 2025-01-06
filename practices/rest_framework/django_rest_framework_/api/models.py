from django.db import models

# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}. Created at:{self.date}'

