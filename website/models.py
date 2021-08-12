from django.db import models
from django import forms




# Create your models here.
class Vehicle(models.Model):
    make = forms.CharField(max_length=30)
    model = forms.CharField(max_length=30)
    is_new = forms.CharField(max_length=3)
    body_type = forms.CharField(max_length=30)
    fuel_type = forms.CharField(max_length=30)
    exterior_color = forms.CharField(max_length=30)
    transmission = forms.CharField(max_length=30)
    wheel_system = forms.CharField(max_length=30)
    engine_type = forms.CharField(max_length=30)
    horsepower = forms.IntegerField()
    engine_displacement = forms.IntegerField()
    mileage = forms.IntegerField()
    transmission_display = forms.IntegerField()
    year = forms.IntegerField()
    fuel_tank_volume = forms.IntegerField()
    city_fuel_economy = forms.FloatField()
    highway_fuel_economy = forms.FloatField()
    maximum_seating = forms.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.make, self.fuel_type)