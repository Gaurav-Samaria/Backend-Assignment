from asyncio.windows_events import NULL
from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=150)
    species = models.CharField(max_length=100)
    weight = models.FloatField()
    length = models.FloatField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name