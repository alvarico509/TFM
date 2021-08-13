import json
import os
from django.conf import settings


def readJson(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def get_make():
    """ GET MAKE SELECTION """
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
    filepath = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/make_model_A.json'
    all_data = readJson(filepath)

    all_models = []

    for x in all_data:
        if x['make_name'] == make:
            y = (x['model_name'], x['model_name'])
            all_models.append(x['model_name'])

    return all_models


def return_body_type(make, model):
    """ GET MODEL SELECTION BY MAKE INPUT """
    filepath = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/web_dic.json'
    all_data = readJson(filepath)

    all_bodies = []

    for x in all_data:
        if (x['make_name'] == make) and x['model_name'] == model:
            if x['body_type'] not in all_bodies:
                all_bodies.append(x['body_type'])

    return all_bodies





filepath_2 = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/web_dic.json'

def return_engine_displacement(make, model, body, fuel, transmission, horsepower):
    all_data = readJson(filepath_2)

    all_displacements = []

    for x in all_data:
        if (x['make_name'] == make) and (x['model_name'] == model) and (x['body_type'] == body) and (x['fuel_type'] == fuel)  and (x['transmission'] == transmission) and (x['horsepower'] == horsepower):
            if x['engine_displacement'] not in all_displacements:
                all_displacements.append(x['engine_displacement'])

    return all_displacements


a = return_engine_displacement('Audi', 'A4', 'Convertible', 'Gasoline', 'A', 170)
print(a)











