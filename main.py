import os
import json
import state
from initView import InitView

state = state.State()

APP_PATH = os.getcwd()
state.app_path = APP_PATH

role = {'1': 'Presidente', '2': 'Médico', '3': 'Técnico', '4': 'Preparadores Físicos', '5': 'Motoristas',
        '6': 'Cozinheiros', '7': 'Advogados', '8': 'Jogador'}

# Definição do caminho e criação do arquivo para registrar os funcionários
EMPLOYEES_JSON_PATH = os.path.join(APP_PATH, 'employees.json')
state.employees_json_path = EMPLOYEES_JSON_PATH

if not os.path.isfile(EMPLOYEES_JSON_PATH):
    employees_data = {
        'presidente': [],
        'medicos': [],
        'tecnicos': [],
        'preparadores': [],
        'motoristas': [],
        'cozinheiros': [],
        'advogados': [],
        'jogadores': [],
    }

    with open(EMPLOYEES_JSON_PATH, 'w') as file:
        json.dump(employees_data, file)

# Definição do caminho e criação do arquivo para registrar os sócios
FAN_PARTNER_JSON_PATH = os.path.join(APP_PATH, 'fan_partners.json')
state.fan_partners_json_path = FAN_PARTNER_JSON_PATH

if not os.path.isfile(FAN_PARTNER_JSON_PATH):
    fan_partners_data = {
        'junior': [],
        'senior': [],
        'elite': []
    }

    with open(FAN_PARTNER_JSON_PATH, 'w') as file:
        json.dump(fan_partners_data, file)

# Definição do caminho e criação do arquivo para registrar os recursos
RESOURCES_JSON_PATH = os.path.join(APP_PATH, 'resources.json')
state.resources_json_path = RESOURCES_JSON_PATH

if not os.path.isfile(RESOURCES_JSON_PATH):
    resources_data = {
        'stadium': [],
        'bus': [],
        'trainingCenter': []
    }

    with open(RESOURCES_JSON_PATH, 'w') as file:
        json.dump(resources_data, file)

view = InitView(state)
state.running = True
state.view = view

while state.running:
    option = state.prompt()
    state.run(option)
