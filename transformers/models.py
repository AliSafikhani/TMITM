
# transformers/models.py

from django.db import models

class Transformer(models.Model):
    name = models.CharField(max_length=100)
    voltage = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    operation_year=models.CharField(max_length=100)
    image_url = models.CharField(max_length=100, blank=True, null=True)  # Add this line
    def __str__(self):
        return self.name


from django.db import models

class TimeSeriesData(models.Model):
    timestamp_r = models.FloatField(default=0.0)
    value_r = models.FloatField(default=0.0)
    timestamp_s = models.FloatField(default=0.0)
    value_s = models.FloatField(default=0.0)
    timestamp_t = models.FloatField(default=0.0)
    value_t = models.FloatField(default=0.0)



