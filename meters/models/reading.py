from django.db import models

class Reading(models.Model):
    mpan = models.CharField(max_length=13)
    meter_id = models.CharField(max_length=10)
    register_id = models.CharField(max_length=2)
    reading = models.DecimalField(max_digits=9, decimal_places=1)
    reading_timestamp = models.DateTimeField()
    filename = models.CharField(max_length=255)

    class Meta:
        unique_together = (('meter_id', 'register_id', 'reading_timestamp'))