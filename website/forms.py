from django import forms
from .models import Vehicle
import json
import os
from django.conf import settings


json_folder = settings.BASE_DIR / 'JSON'
filepath = os.path.join(json_folder, os.path.basename("make_model_A.json"))

def readJson(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def get_make():
    """ GET MAKE SELECTION """
    all_data = readJson(filepath)
    all_makes = []

    for x in all_data:
        if (x['make_name'], x['make_name']) in all_makes:
            continue
        else:
            y = (x['make_name'], x['make_name'])
            all_makes.append(y)

    return all_makes


IS_NEW_CHOICES = [
    ('1', 'Barely new'),
    ('0', 'Used'),
    ]

BODY_TYPE_CHOICES = [
    ('Convertible', 'Convertible'),
    ('Coupe', 'Coupe'),
    ('Hatchback', 'Hatchback'),
    ('Minivan', 'Minivan'),
    ('Pickup Truck', 'Pickup Truck'),
    ('SUV / Crossover', 'SUV / Crossover'),
    ('Sedan', 'Sedan'),
    ('Van', 'Van'),
    ('Wagon', 'Wagon'),
]

FUEL_TYPE_CHOICES = [
    ('Gasoline', 'Gasoline'),
    ('Diesel', 'Diesel'),
    ('Hybrid', 'Hybrid'),
    ('Biodiesel', 'Biodiesel'),
    ('Compressed Natural Gas', 'Compressed Natural Gas'),
    ('Flex Fuel Vehicle', 'Flex Fuel Vehicle'),
]

EXTERIOR_COLOR_CHOICES = [
    ('BLACK', 'Black'),
    ('BLUE', 'Blue'),
    ('BROWN', 'Brown'),
    ('GOLD', 'Gold'),
    ('GRAY', 'Gray'),
    ('GREEN', 'Green'),
    ('ORANGE', 'Orange'),
    ('PINK', 'Pink'),
    ('PURPLE', 'Purple'),
    ('RED', 'Red'),
    ('SILVER', 'Silver'),
    ('TEAL', 'Teal'),
    ('UNKNOWN', 'Other'),
    ('WHITE', 'White'),
    ('YELLOW', 'Yellow'),
]

TRANSMISSION_CHOICES = [
    ('A', 'Automatic (A)'),
    ('M', 'Manual (M)'),
    ('Dual Clutch', 'Dual Clutch Transmission (DCT)'),
    ('CVT', 'Continuously Variable Transmission (CVT)'),
]

WHEEL_SYSTEM_CHOICES = [
    ('RWD', 'Rear Wheel Drive (RWD)'),
    ('FWD', 'Forward Wheel Drive (FWD)'),
    ('AWD', 'All Wheel Drive (AWD)'),
    ('4WD', '4 Wheel Drive (4WD)'),
    ('4x2', '2 Wheel Drive (4x2)'),
]

ENGINE_TYPE_CHOICES = [
    ('I2', 'Inline 2 cylinders'),
    ('I3', 'Inline 3 cylinders'),
    ('I4', 'Inline 4 cylinders'),
    ('I5', 'Inline 5 cylinders'),
    ('I6', 'Inline 6 cylinders'),
    ('H4', 'Horizontal 4 cylinders'),
    ('H6', 'Horizontal 6 cylinders'),
    ('V6', 'V6'),
    ('V8', 'V8'),
    ('V10', 'V10'),
    ('V12', 'V12'),
    ('W12', 'W12'),
    ('W16', 'W16'),
]

class VehicleForm(forms.ModelForm):
    make = forms.ChoiceField(
                    choices = get_make(),
                    required = True,
                    label='Make:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_make'}),
                    )
    is_new = forms.ChoiceField(
                    choices = IS_NEW_CHOICES,
                    required = True,
                    initial = '0',
                    label='Status:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_is_new'}),
                    )
    body_type = forms.ChoiceField(
                    choices = BODY_TYPE_CHOICES,
                    required = True,
                    initial = 'Pickup Truck',
                    label='Body type:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_body_type'}),
                    )
    fuel_type = forms.ChoiceField(
                    choices = FUEL_TYPE_CHOICES,
                    required = True,
                    initial = 'Gasoline',
                    label='Fuel type:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_fuel_type'}),
                    )
    exterior_color = forms.ChoiceField(
                    choices = EXTERIOR_COLOR_CHOICES,
                    required = True,
                    initial = 'BLACK',
                    label='Exterior color:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_exterior_color'}),
                    )
    transmission = forms.ChoiceField(
                    choices = TRANSMISSION_CHOICES,
                    required = True,
                    initial = 'A',
                    label='Transmission:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_is_new'}),
                    )
    wheel_system = forms.ChoiceField(
                    choices = WHEEL_SYSTEM_CHOICES,
                    required = True,
                    initial = '4WD',
                    label = 'Wheel system:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_wheel_system'}),
                    )
    engine_type = forms.ChoiceField(
                    choices = ENGINE_TYPE_CHOICES,
                    required = True,
                    initial = 'V6',
                    label='Engine type:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_engine_type'}),
                    )
    horsepower = forms.ChoiceField(
                    required=True,
                    initial=365,
                    choices=[(x, x) for x in range(55, 1002)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_horsepower'}),
                    )
    engine_displacement = forms.ChoiceField(
                    required=True,
                    initial=3500,
                    choices=[(x, x) for x in range(700, 8500, 100)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_engine_displacement'}),
                    )
    mileage = forms.IntegerField(
                    required = True,
                    label = 'Mileage:',
                    initial = 66211,
                    max_value = 1000000,
                    min_value = 0,
                    widget = forms.NumberInput(attrs={'class': 'form-control', 
                                                      'id': 'id_mileage', 
                                                      'step': "1"}),
                    )
    transmission_display = forms.ChoiceField(
                    required=True,
                    initial=6,
                    choices=[(x, x) for x in range(1, 11)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_transmission_display'}),
                    )
    year = forms.ChoiceField(
                    required=True,
                    initial=2015,
                    choices=[(x, x) for x in range(1915, 2022)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_year'}),
                    )
    fuel_tank_volume = forms.ChoiceField(
                    required=True,
                    initial=36,
                    choices=[(x, x) for x in range(1, 65)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_fuel_tank_volume'}),
                    )
    city_fuel_economy = forms.ChoiceField(
                    required=True,
                    initial=17,
                    choices=[(x, x) for x in range(7, 128)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_city_fuel_economy'}),
                    )
    highway_fuel_economy = forms.ChoiceField(
                    required=True,
                    initial=23,
                    choices=[(x, x) for x in range(10, 128)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_highway_fuel_economy'}),
                    )
    maximum_seating = forms.ChoiceField(
                    required=True,
                    initial=5,
                    choices=[(x, x) for x in range(2, 16)],
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_maximum_seating'}),
                    )


    class Meta:
            model = Vehicle
            fields = ['make', 'is_new', 'body_type', 'fuel_type', 'exterior_color', 'transmission', 'wheel_system', 'engine_type',
                      'horsepower', 'engine_displacement', 'mileage', 'transmission_display', 'year', 'fuel_tank_volume',
                      'city_fuel_economy', 'highway_fuel_economy', 'maximum_seating']
