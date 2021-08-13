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


class VehicleForm(forms.ModelForm):
    make = forms.ChoiceField(
                    choices = get_make(),
                    required = True,
                    initial = 'Ford',
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
    exterior_color = forms.ChoiceField(
                    choices = EXTERIOR_COLOR_CHOICES,
                    required = True,
                    initial = 'BLACK',
                    label='Exterior color:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_exterior_color'}),
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
            fields = ['make', 'is_new', 'exterior_color', 'mileage', 'year', 'fuel_tank_volume',
                      'city_fuel_economy', 'highway_fuel_economy', 'maximum_seating']
