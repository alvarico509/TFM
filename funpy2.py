import json
import os
from django.conf import settings



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