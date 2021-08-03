import json
import os
from django.conf import settings



def readJson(filename):
    with open(filename, 'r') as fp:
        return json.load(fp)

def get_country():
    """ GET COUNTRY SELECTION """
    #json_folder = settings.BASE_DIR / "JSON"
    #file_path = os.path.join(json_folder, os.path.basename("countries_states_cities"))
    filepath = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/countries_states_cities.json'
    all_data = readJson(filepath)
    all_countries = [('-----', '---Select a Country---')]

    for x in all_data:
        y = (x['name'], x['name'])
        all_countries.append(y)
    print(all_countries)
    return all_countries

def return_state_by_country(country):
    """ GET STATE SELECTION BY COUNTRY INPUT """
    #json_folder = settings.BASE_DIR / "JSON"
    #file_path = os.path.join(json_folder, os.path.basename("countries_states_cities"))
    filepath = '/Users/alvarolozanoalonso/desktop/project_tfm/tfm/JSON/countries_states_cities.json'
    all_data = readJson(filepath)

    all_states = []

    for x in all_data:
        if x['name'] == country:
            if 'states' in x:
                for state in x['states']:
                    y = (state['name'], state['name'])
                    all_states.append(state['name'])
            else:
                all_states.append(country)
    return all_states

a = return_state_by_country("Spain")
print(a)
get_country()