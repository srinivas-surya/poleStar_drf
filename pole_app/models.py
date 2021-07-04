from django.db import models

# Create your models here.


class ShipData(models.Model):
    name = models.CharField(max_length=160)
    imoNumber = models.CharField(max_length=60)
    time_stamp = models.CharField(max_length=160)
    latitude = models.CharField(max_length=160)
    longitude = models.CharField(max_length=160)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
