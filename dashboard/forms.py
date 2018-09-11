from django import forms
from .models import Transport

from django import forms

class AddInfoForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields = ('driver_first_name',
            'driver_last_name',
            'driver_contact',
            'truck_number',
            'origin_lat',
            'origin_lon',
            'destination_lat',
            'destination_lon',
            'current_location_lat',
            'current_location_lon',
            'last_stoppage_lat',
            'last_stoppage_lot',
            'speed',)



            
