import view
from stateMetaclass import StateMetaclass


class State(metaclass=StateMetaclass):

    def __init__(self):
        self.running = True

    app_path: str
    roles_json_path: str
    resources_json_path: str
    employees_json_path: str
    fan_partners_json_pat: str

    view: view.View

    view_stack = []

    def prompt(self):
        return self.view.prompt()

    def run(self, option):
        self.view.run(option)
