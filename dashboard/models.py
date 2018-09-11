from django.db import models

class Transport(models.Model):
    driver_first_name = models.CharField(max_length=15)
    driver_last_name = models.CharField (max_length=15)
    driver_contact = models.CharField(max_length=10)

    truck_number = models.CharField(max_length=12, default='') # I am not sure about the max length.

    origin_lat = models.DecimalField(max_digits=9, decimal_places=6)
    origin_lon = models.DecimalField(max_digits=9, decimal_places=6)

    destination_lat = models.DecimalField(max_digits=9, decimal_places=6)
    destination_lon = models.DecimalField(max_digits=9, decimal_places=6)

    current_location_lat = models.DecimalField(max_digits=9, decimal_places=6)
    current_location_lon = models.DecimalField(max_digits=9, decimal_places=6)

    last_stoppage_lat = models.DecimalField(max_digits=9, decimal_places=6)
    last_stoppage_lot = models.DecimalField(max_digits=9, decimal_places=6)

    last_update = models.DateTimeField(auto_now_add=True)
    #update when data is first inserted / saved by django form

    speed = models.PositiveIntegerField(default=0);
