from django import forms
from .models import Vehicle
from django.conf import settings
import json
import os


json_folder = settings.BASE_DIR / 'JSON'
filepath_2 = os.path.join(json_folder, os.path.basename("web_dic.json"))

def readJson(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def get_make():
    """ GET MAKE SELECTION """
    all_data = readJson(filepath_2)
    all_makes = []
    all_makes.append(["Empty", "----------Select Make----------"])

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
    ('Black', 'Black'),
    ('Blue', 'Blue'),
    ('Brown', 'Brown'),
    ('Gold', 'Gold'),
    ('Gray', 'Gray'),
    ('Green', 'Green'),
    ('Orange', 'Orange'),
    ('Pink', 'Pink'),
    ('Purple', 'Purple'),
    ('Red', 'Red'),
    ('Silver', 'Silver'),
    ('Teal', 'Teal'),
    ('Unknown', '----------Select Color----------'),
    ('White', 'White'),
    ('Yellow', 'Yellow'),
]


class VehicleForm(forms.ModelForm):
    make = forms.ChoiceField(
                    choices = get_make(),
                    required = True,
                    initial = 'Default',
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
                    initial = 'Unknown',
                    label='Exterior color:',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_exterior_color'}),
                    )
    mileage = forms.IntegerField(
                    required = True,
                    label = 'Mileage:',
                    max_value = 1000000,
                    min_value = 0,
                    widget = forms.NumberInput(attrs={'class': 'form-control', 
                                                      'id': 'id_mileage', 
                                                      'step': "1"}),
                    )


    class Meta:
            model = Vehicle
            fields = ['make', 'is_new', 'exterior_color', 'mileage']
