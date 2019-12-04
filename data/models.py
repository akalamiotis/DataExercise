from django.conf import settings
from django.db import models
from django.utils.timezone import now


class Record(models.Model):
    """
    Contains the record for the file.
    """

    file_type_id = models.CharField(max_length=255)
    company_id = models.CharField(max_length=255)
    file_creation_date = models.DateField()
    file_upload_datetime = models.DateTimeField(default=now)
    file_creation_time = models.TimeField()
    file_gen_number = models.CharField(max_length=255)


class Meter(models.Model):
    """
    Contains meter data.
    """

    record = models.ForeignKey(
        "data.Record",
        on_delete=models.CASCADE,
    )
    
    meter_number = models.CharField(max_length=255)
    measurement_date = models.DateField()
    measurement_time = models.TimeField()
    consumption = models.DecimalField(decimal_places=2, max_digits=6)
