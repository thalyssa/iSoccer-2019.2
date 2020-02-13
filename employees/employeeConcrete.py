from personInterface import PersonInterface
from main import role, state
import json


class EmployeeConcrete(PersonInterface):
    salary: str
    employee_role: str

    def register(self):

        input('Digite as informações do funcionário a ser cadastrado à seguir')
        self.name = input('Nome:')
        self.email = input('E-mail: ')
        self.cpf = input('CPF: ')
        self.salary = input('Salário: ')
        self.phone = input('Telefone: ')

        self.writeOnFile()

        print('Funcionário cadastrado!')

    def defineRole(self, option: str):
        self.employee_role = role[option]

        if option == '2':
            pass
        if option == '5':
            pass
        if option == '8':
            pass
        else:
            self.register()

    def writeOnFile(self):

        with open(state.employees_json_path, 'r') as file:
            employee_info = json.load(file)

        employee_data = {'Nome': self.name, 'E-mail': self.email, 'CPF': self.cpf, 'Salário': self.salary, 'Telefone': self.phone}

        var = employee_info[self.employee_role].append(employee_data)

        with open(state.employees_json_path, 'w') as file:
            json.dump(var, file)

