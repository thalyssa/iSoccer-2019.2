import os
import json
import state

state = state.State()

APP_PATH = os.getcwd()
state.app_path = APP_PATH

RESOURCES_JSON_PATH = os.path.join(APP_PATH, 'resources.json')
state.resources_data_path = RESOURCES_JSON_PATH

if not os.path.isfile(RESOURCES_JSON_PATH):
    resources_data = {
        'stadium': [],
        'bus': [],
        'trainingCenter': []
    }

    with open(RESOURCES_JSON_PATH, 'w') as file:
        json.dump(resources_data, file)
