from django.db import models

# Create your models here.
class Tasks(models.Model):
    task = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.task}'