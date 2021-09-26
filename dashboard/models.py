from django.db import models

# Create your models here.


class Data(models.Model):
    city = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)


    class Meta:
        verbose_name_plural = 'Data'

    def __str__(self):
        return self.city
