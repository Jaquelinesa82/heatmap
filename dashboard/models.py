from django.db import models
import geocoder
# Create your models here.


class Data(models.Model):
    city = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Data'

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.city).lat
        self.longitude = geocoder.osm(self.city).lng
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.city
