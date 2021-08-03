from django import forms
from .models import makeModel
import json

def readJson(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def get_make():
    """ GET MAKE SELECTION """
    #json_folder = settings.BASE_DIR / "JSON"
    #file_path = os.path.join(json_folder, os.path.basename("countries_states_cities"))
    filepath = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/make_model_A.json'
    all_data = readJson(filepath)
    all_makes = [('-----', '---Select a Make---')]

    for x in all_data:
        if (x['make_name'], x['make_name']) in all_makes:
            continue
        else:
            y = (x['make_name'], x['make_name'])
            all_makes.append(y)

    return all_makes

def return_model_by_make(make):
    """ GET MODEL SELECTION BY MAKE INPUT """
    #json_folder = settings.BASE_DIR / "JSON"
    #file_path = os.path.join(json_folder, os.path.basename("countries_states_cities"))
    filepath = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/make_model_A.json'
    all_data = readJson(filepath)

    all_models = []

    for x in all_data:
        if x['make_name'] == make:
            y = (x['model_name'], x['model_name'])
            all_models.append(x['model_name'])

    return all_models


IS_NEW_CHOICES = [
    ('1', 'Yes'),
    ('0', 'No'),
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
    ('UNKNOWN', 'Unknown'),
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

class ContactForm(forms.Form):
    your_name = forms.CharField(max_length=30)
    make_name = forms.ChoiceField(
                    choices = get_make(),
                    required = True,
                    label='This is the make!',
                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'id_make_name'}),
                    )
    class Meta:
            model = makeModel
            fields = ('make_name', 'model_name')

    is_new = forms.CharField(label='Is the car (barely) new?', widget=forms.Select(choices=IS_NEW_CHOICES))
    body_type = forms.CharField(label='What is the type of the car?', widget=forms.Select(choices=BODY_TYPE_CHOICES))
    fuel_type = forms.CharField(widget=forms.Select(choices=FUEL_TYPE_CHOICES))
    exterior_color = forms.CharField(widget=forms.Select(choices=EXTERIOR_COLOR_CHOICES))
    transmission = forms.CharField(widget=forms.Select(choices=TRANSMISSION_CHOICES))
    wheel_system = forms.CharField(widget=forms.Select(choices=WHEEL_SYSTEM_CHOICES))
    engine_type = forms.CharField(widget=forms.Select(choices=ENGINE_TYPE_CHOICES))
    horsepower = forms.IntegerField(required=True, initial=200, widget=forms.NumberInput(attrs={'id': 'form_horsepower', 'step': "1"}))
    engine_displacement = forms.IntegerField(required=True, initial=3800, widget=forms.NumberInput(attrs={'id': 'form_engine_displacement', 'step': "1"}))
    mileage = forms.IntegerField(required=True, initial=30000, widget=forms.NumberInput(attrs={'id': 'form_mileage', 'step': "1"}))
    transmission_display = forms.IntegerField(required=True, initial=6, widget=forms.NumberInput(attrs={'id': 'form_transmission_display', 'step': "1"}))
    year = forms.IntegerField(required=True, initial=2010, widget=forms.NumberInput(attrs={'id': 'form_year', 'step': "1"}))
    fuel_tank_volume = forms.IntegerField(required=True, initial=30, widget=forms.NumberInput(attrs={'id': 'form_fuel_tank_volume', 'step': "1"}))
    city_fuel_economy = forms.FloatField(required=True, initial=20, widget=forms.NumberInput(attrs={'id': 'form_city_fuel_economy', 'step': "0.1"}))
    highway_fuel_economy = forms.FloatField(required=True, initial=20, widget=forms.NumberInput(attrs={'id': 'form_highway_fuel_economy', 'step': "0.1"}))
    maximum_seating = forms.IntegerField(required=True, initial=5, widget=forms.NumberInput(attrs={'id': 'form_maximum_seating', 'step': "1"}))

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        is_new = cleaned_data.get('is_new')
        body_type = cleaned_data.get('body_type')
        fuel_type = cleaned_data.get('fuel_type')
        exterior_color = cleaned_data.get('exterior_color')
        transmission = cleaned_data.get('transmission')
        wheel_system = cleaned_data.get('wheel_system')
        engine_type = cleaned_data.get('engine_type')
        horsepower = cleaned_data.get('horsepower')
        engine_displacement = cleaned_data.get('engine_displacement')
        mileage = cleaned_data.get('mileage')
        transmission_display = cleaned_data.get('transmission_display')
        year = cleaned_data.get('year')   
        fuel_tank_volume = cleaned_data.get('fuel_tank_volume')
        city_fuel_economy = cleaned_data.get('city_fuel_economy')
        highway_fuel_economy = cleaned_data.get('highway_fuel_economy')
        maximum_seating = cleaned_data.get('maximum_seating')
        if (not your_name and not horsepower and not engine_displacement and not mileage and not transmission_display and 
            not year and not fuel_tank_volume and not city_fuel_economy and not highway_fuel_economy and not maximum_seating
            and not is_new and not body_type and not fuel_type and not exterior_color and not transmission and not wheel_system
            and not engine_type):
            raise forms.ValidationError('Some fields have errors!')


    



            





